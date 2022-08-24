from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.auth.schemas import UserOut, UserAuth, TokenSchema, SystemUser
from app.auth.deps import get_current_user
from app.auth.utils import ( 
    get_hashed_password,
    verify_password,
    create_access_token,
    create_refresh_token
)
from uuid import uuid4

#From fake db
from app.auth.fake_db import users_db

router = APIRouter()

@router.post('/signup', summary="Create new user", response_model=UserOut)
async def create_user(data: UserAuth):
    # search on fake database to check if user already exist
    user = next((user for user in users_db if user['email'] == data.email), None)
    if user is not None:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exist"
        )
    user = {
        'email': data.email,
        'password': get_hashed_password(data.password),
        'id': str(uuid4())
    }
    
    # Fake save on db
    users_db.append(user)
    return user

@router.post('/login', summary="Create access and refresh tokens for user", response_model=TokenSchema)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # search user on fake db
    user = next((user for user in users_db if user['email'] == form_data.username), None)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    hashed_pass = user['password']
    if not verify_password(form_data.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    
    return {
        "access_token": create_access_token(user['email']),
        "refresh_token": create_refresh_token(user['email']),
    }

@router.get('/me', summary='Get details of currently logged in user', response_model=UserOut)
async def get_me(user: SystemUser = Depends(get_current_user)):
    return user
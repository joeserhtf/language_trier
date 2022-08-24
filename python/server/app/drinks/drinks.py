from fastapi import APIRouter, status, HTTPException, Depends
from app.auth.deps import get_current_user
from app.drinks.schemas import Drink

router = APIRouter(
    prefix="/drinks",
    tags=["drinks"],
    dependencies=[Depends(get_current_user)],
    responses={404: {"description": "Not found"}},
)

drinksData = [
        {
            "id": 1,
            "name": "Margarita",
            "description": "Cloyingly sweet margarita mixes have given this drink a bad name. A well-made version is a fresh mix of lime juice and tequila, with a hint of sweetener.",
            "image": "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/margarita-1592951298.jpg",
            "observations": [
                "light",
                "sweet",
                "fresh",
                "acid"
            ]
        },
        {
            "id": 2,
            "name": "Martini",
            "description": "James Bond was wrong—whether you drink it with gin or vodka, stirred is the way to go when ordering a martini.",
            "image": "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/martini-1592951711.jpg",
            "observations": [
                "strong",
                "dry",
                "spices"
            ]
        }
    ]

@router.get("")
async def drinks():
    return drinksData

@router.post("")
async def drinks(drink: Drink):
    # Not need validate class already does that
    drinksData.append(drink)

    return drinksData
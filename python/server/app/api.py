from fastapi import FastAPI
from .auth import auth
from .drinks import drinks

app = FastAPI()

app.include_router(auth.router)
app.include_router(drinks.router)

@app.get("/ping")
async def root():
    return {
		"message": "pong",
    }
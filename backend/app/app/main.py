from fastapi import FastAPI
from app.routers import predictions


app = FastAPI()

app.include_router(predictions.router)

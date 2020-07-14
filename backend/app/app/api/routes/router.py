from fastapi import APIRouter

from app.api.routes import heartbeat, predictions

api_router = APIRouter()
api_router.include_router(heartbeat.router, tags=["health"])
api_router.include_router(predictions.router, tags=["prediction"])

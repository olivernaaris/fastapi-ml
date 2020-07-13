from fastapi import APIRouter, HTTPException
from app.machine_learning.model import convert, predict
from app.models.payload import stockin, stockout

router = APIRouter()


@router.get("/ping")
async def pong():
    return {"ping": "pong!"}


@router.post("/predict", response_model=stockout, status_code=200)
async def get_prediction(payload: stockin):
    ticker = payload.ticker

    prediction_list = predict(ticker)

    if not prediction_list:
        raise HTTPException(status_code=400, detail="Model not found.")

    response_object = {"ticker": ticker, "forecast": convert(prediction_list)}
    return response_object

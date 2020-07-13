from fastapi import APIRouter, HTTPException
from app.machine_learning.model import convert, PredictStocks
from app.models.payload import StockIn, StockOut

router = APIRouter()


@router.get("/ping")
async def pong():
    return {"ping": "pong!"}


@router.post("/predict", response_model=StockOut, status_code=200)
async def get_prediction(payload: StockIn):
    ticker = payload.ticker

    prediction_list = PredictStocks(ticker)

    if not prediction_list:
        raise HTTPException(status_code=400, detail="Model not found.")

    response_object = {"ticker": ticker, "forecast": convert(prediction_list.result)}
    return response_object

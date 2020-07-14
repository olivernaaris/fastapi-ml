from fastapi import APIRouter, HTTPException
from app.machine_learning.model import convert, PredictStocks
from app.models.payload import StockIn, StockOut

router = APIRouter()


async def _get_prediction(ticker):  # A function defined by async def is a native coprocess object
    return PredictStocks(ticker)    # See - https://programmer.ink/think/latest-python-asynchronous-programming-explanation.html


@router.post("/predict", response_model=StockOut, status_code=200)
async def get_prediction(payload: StockIn):
    ticker = payload.ticker

    prediction_list = await _get_prediction(ticker) # Here _get_prediction(ticker) is a native collaboration object

    if not prediction_list:
        raise HTTPException(status_code=400, detail="Model not found.")

    response_object = {"ticker": ticker, "forecast": convert(prediction_list.result)}
    return response_object

from pydantic import BaseModel

# Pydantic models


class StockIn(BaseModel):
    ticker: str


class StockOut(StockIn):
    forecast: dict

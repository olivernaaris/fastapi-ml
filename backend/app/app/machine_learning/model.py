import datetime
from pathlib import Path

import joblib
import pandas as pd
import yfinance as yf
from fbprophet import Prophet

BASE_DIR = Path(__file__).resolve(strict=True).parent
TODAY = datetime.date.today()


def convert(prediction_list):
    output = {}
    for data in prediction_list:
        date = data["ds"].strftime("%m/%d/%Y")
        output[date] = data["trend"]
    return output


class PredictStocks(object):

    def __init__(self, ticker="MSFT"):
        self.ticker = ticker

    def train(self):
        # data = yf.download("^GSPC", "2008-01-01", TODAY.strftime("%Y-%m-%d"))
        data = yf.download(self.ticker, "2020-01-01", TODAY.strftime("%Y-%m-%d"))
        data.head()
        data["Adj Close"].plot(title=f"{self.ticker} Stock Adjusted Closing Price")

        df_forecast = data.copy()
        df_forecast.reset_index(inplace=True)
        df_forecast["ds"] = df_forecast["Date"]
        df_forecast["y"] = df_forecast["Adj Close"]
        df_forecast = df_forecast[["ds", "y"]]
        df_forecast

        model = Prophet()
        model.fit(df_forecast)

        joblib.dump(model, Path(BASE_DIR).joinpath(f"{self.ticker}.joblib"))

    def predict(self, days=7):
        model_file = Path(BASE_DIR).joinpath(f"{self.ticker}.joblib")
        if not model_file.exists():
            return False

        model = joblib.load(model_file)

        future = TODAY + datetime.timedelta(days=days)

        dates = pd.date_range(start="2020-01-01", end=future.strftime("%m/%d/%Y"),)
        df = pd.DataFrame({"ds": dates})

        forecast = model.predict(df)

        model.plot(forecast).savefig(f"{self.ticker}_plot.png")
        model.plot_components(forecast).savefig(f"{self.ticker}_plot_components.png")

        return forecast.tail(days).to_dict("records")

    result = property(predict)



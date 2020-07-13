from fastapi import FastAPI

from app.routers import predictions
from app.core.config import (API_PREFIX, APP_NAME, APP_VERSION, IS_DEBUG)
from app.core.event_handlers import (start_app_handler, stop_app_handler)


def get_app() -> FastAPI:
    fastapi_ml = FastAPI(title=APP_NAME, version=APP_VERSION, debug=IS_DEBUG)
    fastapi_ml.include_router(predictions.router)

    fastapi_ml.add_event_handler("startup", start_app_handler(fastapi_ml))
    fastapi_ml.add_event_handler("shutdown", stop_app_handler(fastapi_ml))

    return fastapi_ml


app = get_app()

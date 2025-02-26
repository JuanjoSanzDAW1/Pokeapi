from fastapi import FastAPI
from middleware.logger_middleware import log_requests_middleware
from view.routes import router
import sentry_sdk
from redis_config import set_value, get_value


sentry_sdk.init(
    dsn="https://0bab9bcfd1d293a21edbaffe31f1f6f8@o4508609329692672.ingest.de.sentry.io/4508609527480400",
    traces_sample_rate=1.0,
)


app = FastAPI()

#
@app.middleware("http")
async def logger_middleware(request, call_next):
    return await log_requests_middleware(request, call_next)



app.include_router(router)


@app.get("/sentry-debug")
async def trigger_error():
    division_by_zero = 1 / 0


@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/redis-test")
async def redis_test():
    set_value("test_key", "Hello from Redis!")
    value = get_value("test_key")
    return {"stored_value": value}


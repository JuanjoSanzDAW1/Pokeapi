from fastapi import FastAPI
from middleware.logger_middleware import log_requests_middleware
from view.routes import router
import sentry_sdk

# Inicializar Sentry SDK
sentry_sdk.init(
    dsn="https://0bab9bcfd1d293a21edbaffe31f1f6f8@o4508609329692672.ingest.de.sentry.io/4508609527480400",
    traces_sample_rate=1.0,  # Captura el 100% de las transacciones para trazas
)

# Inicializar la aplicación FastAPI
app = FastAPI()

# Configurar Middleware
@app.middleware("http")
async def logger_middleware(request, call_next):
    return await log_requests_middleware(request, call_next)

# Registrar las rutas desde el enrutador
app.include_router(router)

# Ruta para probar Sentry (solo para depuración)
@app.get("/sentry-debug")
async def trigger_error():
    division_by_zero = 1 / 0

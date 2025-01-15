import uuid
import logging
from datetime import datetime
from fastapi import Request
from fastapi.responses import JSONResponse


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(request_id)s - %(api_call)s - %(message)s",
)
logger = logging.getLogger(__name__)

class RequestIDFilter(logging.Filter):

    def __init__(self, request_id: str):
        super().__init__()
        self.request_id = request_id

    def filter(self, record):
        record.request_id = self.request_id
        return True

async def log_requests_middleware(request: Request, call_next):


    request_id = str(uuid.uuid4())


    filter = RequestIDFilter(request_id)
    logger.addFilter(filter)


    api_call = f"{request.method} {request.url.path}"
    timestamp = datetime.utcnow().isoformat()


    logger.info(f"Request received: {api_call}", extra={"api_call": api_call, "timestamp": timestamp})

    try:

        response = await call_next(request)
    except Exception as e:

        logger.error(f"Error occurred: {str(e)}", extra={"api_call": api_call, "timestamp": timestamp})
        return JSONResponse(content={"error": "Internal Server Error"}, status_code=500)
    finally:

        logger.info(f"Response sent: {api_call}", extra={"api_call": api_call, "timestamp": timestamp})


        logger.removeFilter(filter)

    return response

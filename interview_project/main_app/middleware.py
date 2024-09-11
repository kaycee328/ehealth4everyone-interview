import time
import logging

logger = logging.getLogger("request_logger")


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        response = self.get_response(request)

        duration = time.time() - start_time
        log_data = {
            "user": (
                request.user.username if request.user.is_authenticated else "Anonymous"
            ),
            "method": request.method,
            "path": request.path,
            "status_code": response.status_code,
            "duration": duration,
        }

        logger.info(log_data)
        return response

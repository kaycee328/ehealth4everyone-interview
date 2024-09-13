from rest_framework.response import Response
from rest_framework.decorators import APIView
from django.core.cache import cache
from datetime import datetime
from rest_framework.permissions import IsAuthenticated
import time
import random


class AssignmentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        start_time = datetime.now()

        # Cache key, here we can bust based on user id
        cache_key = f"user_{request.user.id}_data"

        # Check if response is cached
        data = cache.get(cache_key)

        if not data:
            # Simulate time consuming computation
            time.sleep(random.randint(1, 5))
            data = {"message": "A response!"}
            cache.set(cache_key, data, timeout=60 * 5)  # Cache for 5 minutes

        end_time = datetime.now()
        total_duration = end_time - start_time

        # Log request and response details in a readable format
        log_data = {
            "user": str(request.user),
            "start_time": start_time.strftime("%Y-%m-%d %H:%M:%S"),
            "end_time": end_time.strftime("%Y-%m-%d %H:%M:%S"),
            "total_duration": str(total_duration),  # timedelta as string (HH:MM:SS)
            "request_method": request.method,
            "request_url": request.build_absolute_uri(),
            "response_status": 200,
        }

        # Log to file
        with open("request_logs.txt", "a") as log_file:
            log_file.write(f"{log_data}\n")

        return Response(data)

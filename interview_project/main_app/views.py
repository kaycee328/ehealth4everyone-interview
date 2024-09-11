from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView


class ExampleView(APIView):
    def get(self, request, *args, **kwargs):
        cache_key = f"example_data_{request.user.id}"
        data = cache.get(cache_key)

        if not data:
            # Fetch the data from the database or external API
            data = {"example": "value"}

            # Set cache with a timeout of 5 minutes
            cache.set(cache_key, data, timeout=300)

        return Response(data)

    def get_cache_key(request):
        role = "admin" if request.user.is_staff else "user"
        return f"data_{request.user.id}_{role}_{request.GET.get('version', 'v1')}"

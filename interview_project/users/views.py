from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.authentication import BasicAuthentication
from .serializers import CreateUserSerializer, LoginUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken


# Signup view for user login
class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]
    authentication_classes = [BasicAuthentication]  # Basic Authentication for API


# Login view for user login
class LoginView(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, format=None):
        # Use the serializer to validate the request data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Retrieve the validated user from the serializer
        user = serializer.validated_data["user"]

        # Generate refresh and access tokens
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "username": user.username,
                "user_id": user.id,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            status=status.HTTP_200_OK,
        )

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import RegistrationSerializer


class RegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)

        data = {}
        if serializer.is_valid():
            saved_account = serializer.save()
            data = {
                'username': saved_account.username,
                'email': saved_account.email,
                'user_id': saved_account.pk
            }
            return Response(data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Test view to verify JWT authentication
from rest_framework.permissions import IsAuthenticated


class HelloWorldView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Hello, World!"})


from rest_framework_simplejwt.views import TokenObtainPairView


class CookieTokenObtainPairView(TokenObtainPairView):
    """
    Custom view to obtain JWT tokens and set them in HttpOnly cookies.
    """
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        # Set the tokens in HttpOnly cookies
        refresh = response.data.get('refresh')
        # Retrieve the access token from the response data
        access = response.data.get('access')

        # Set cookies for access token
        response.set_cookie(
            key="access_token",  # Name of the cookie
            value=access,  # The JWT access token
            httponly=True,  # Prevents JavaScript access to the cookie
            secure=True,  # Set to True in production with HTTPS
            samesite='Lax'  # Adjust based on your requirements
        )

        # Set cookies for refresh token
        response.set_cookie(
            key="refresh_token",
            value=refresh,
            httponly=True,
            secure=True,
            samesite='Lax'
        )

        response.data = {"message": "Login erfolgreich"}
        return response

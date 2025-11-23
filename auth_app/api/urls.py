from django.urls import path

# Importing JWT views for token handling
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    RegistrationView,
    HelloWorldView,
    CookieTokenObtainPairView,
    CookieTokenRefreshView,
)


urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    # JWT token endpoints
    path('token/', CookieTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Endpoint to refresh JWT tokens
    path('token/refresh/', CookieTokenRefreshView.as_view(), name='token_refresh'),

    # Test endpoint to verify JWT authentication
    path('hello/', HelloWorldView.as_view(), name='hello_world'),
]

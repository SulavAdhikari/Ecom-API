from django.urls import path
from .views import UserRegistrationView, UserLoginView, AuthTestView, PasswordResetAPIView, PasswordResetConfirmAPIView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('isauth/', AuthTestView.as_view(), name='authentication-test'),
     path('password-reset/confirm/<uidb64>/<token>', PasswordResetConfirmAPIView.as_view(), name='password_reset_confirm'),
     path('forgot-password/', PasswordResetAPIView.as_view(), name='password_reset'),

    # Add other URL patterns as needed
]

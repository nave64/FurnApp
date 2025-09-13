# account_module/urls.py

from django.urls import path
from .views import RegisterView, OTPVerificationView, LoginPageView, LogoutView, ForgetPasswordView, VerificationResetPasswordView, ResetPasswordView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register_page'),
    path('otp-verify/', OTPVerificationView.as_view(), name='otp_verify_page'),
    path('login/', LoginPageView.as_view(), name='login_page'),
    path('logout/', LogoutView.as_view(), name='logout_page'),
    path('forgot-password/', ForgetPasswordView.as_view(), name='forget_password_page'),
    path('verification-reset-password/', VerificationResetPasswordView.as_view(), name='verification_reset_password_page'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset_password_page'),
]

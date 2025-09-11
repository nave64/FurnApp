# account_module/urls.py

from django.urls import path
from .views import RegisterView, OTPVerificationView, LoginPageView, LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register_page'),
    path('otp-verify/', OTPVerificationView.as_view(), name='otp_verify_page'),
    path('login/', LoginPageView.as_view(), name='login_page'),
    path('logout/', LogoutView.as_view(), name='logout_page'),  # 👈 ADD THIS

]

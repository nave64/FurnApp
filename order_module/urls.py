from django.urls import path
from . import views
from .views import SamanEPayView, SamanEPayCallbackView

urlpatterns = [
    # Product order management
    path('add-to-order', views.add_product_to_order, name='add_product_to_order'),
    
    # New Zarinpal payment system
    path('payment/', views.PaymentView.as_view(), name='payment_form'),
    path('order-payment/', views.OrderPaymentView.as_view(), name='order_payment_new'),
    path('payment-verify/', views.PaymentVerifyView.as_view(), name='payment_verify'),
    path('payment-history/', views.PaymentHistoryView.as_view(), name='payment_history'),
    
    # Legacy payment views (for backward compatibility)
    path('pay/', views.OrderPayView.as_view(), name='order_payment'),
    path('verify/', views.VerifyPayView.as_view(), name='verify'),
    path('callback/', views.CallbackView.as_view(), name='payment_callback'),
    
    # SamanEPay payment system
    path('samanepay/', SamanEPayView.as_view(), name='samanepay_payment'),
    path('samanepay-callback/', SamanEPayCallbackView.as_view(), name='samanepay_callback'),
]

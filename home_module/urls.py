from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index_page_urls'),
    path('rules/', views.rules_page, name='rules_page'),
    path('shipment/', views.shipment_page, name='shipment_page'),
    path('payment-methods/', views.payment_methods_page, name='payment_methods_page'),
    path('refund-terms/', views.refund_terms_page, name='refund_terms_page'),
]
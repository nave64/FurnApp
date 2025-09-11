from django.urls import path
from . import views
from product_module.views import ProductDetailView
from .views import EditUserProfilePage, UserImageUploadView

urlpatterns = [
    path('', views.UserPanelDashboardPage.as_view(), name='user_panel_urls'),
    path('edit-profile/', EditUserProfilePage.as_view(), name='edit-user-profile_urls'),
    path('change-pass', views.ChangePasswordPage.as_view(), name='change_password_page_urls'),
    path('user-basket', views.user_basket, name='user_basket_page'),
    path('my-shoppings', views.MyShoppingsView.as_view(), name='user_shoppings_page'),
    path('upload-images/', UserImageUploadView.as_view(), name='user_upload_images_page'),

    path('my-shoppings-detail/<order_id>', views.my_shopping_detail, name='user_shoppings_detail_page'),
    path('remove-order-detail', views.remove_order_detail, name='remove_order_detail_ajax'),
    path('change-order-detail', views.change_order_detail_count, name='change_order_detail_count_ajax'),
    path('get-cart-count/', views.get_cart_count, name='get_cart_count_ajax'),
]
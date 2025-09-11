from django.urls import path, re_path
from . import views
from .views import ProductDetailView

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('search/', views.search, name='search'),
    path('cat/<cat>', views.ProductListView.as_view(), name='product-categories_list'),
    path('brand/<brand>', views.ProductListView.as_view(), name='product-list-by-brands'),
    path('product-favorite', views.AddProductFavorite.as_view(), name='product-favorite'),
    path('add-comment/<int:product_id>/', views.add_product_comment, name='add_product_comment'),
    path('compare/', views.CompareProductsView.as_view(), name='compare_products'),
    path('add-to-compare/', views.AddToCompareView.as_view(), name='add_to_compare'),
    path('compare/clear/', views.clear_compare_list, name='clear_compare'),
    path('add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('list/', views.wishlist_page, name='wishlist_page'),

    ## ✅ IMPORTANT: Catch-all slug route must always be LAST!
    re_path(r'^(?P<slug>[-\wآ-یءئ]+)/$', ProductDetailView.as_view(), name='product_detail'),
]

from django.urls import path
from . import views
from .views import ContactUsView

urlpatterns = [
    path('', ContactUsView.as_view(), name='contact_page_urls'),
    path('register', views.CreateProfileView.as_view(), name='register'),
    path('Profiles-view', views.ProfilesView.as_view(), name='profiles_view')
]
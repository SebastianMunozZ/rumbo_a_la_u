from django.urls import path, include
from rest_framework import routers
from api import views
from .views import UserViewSet


urlpatterns = [
    path('login/', UserViewSet.as_view({'post': 'login'}), name='login'),
    path('register/', UserViewSet.as_view({'post': 'create'}), name='create')
]

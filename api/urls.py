from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
]
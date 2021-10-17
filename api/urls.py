from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('user', views.UserEditViewSet)
router.register('diary', views.DiaryViewSet)
router.register('page', views.PageViewSet)

urlpatterns = [
    path('register/', views.CreateUserView.as_view(), name='register'),
    path('', include(router.urls)),
]

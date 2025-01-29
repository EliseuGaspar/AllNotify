from rest_framework.routers import DefaultRouter
from django.urls import include, path

from Users.views import UserViewSet

router = DefaultRouter()

router.register(r"", UserViewSet, basename="user-router")

urlpatterns = [
    path("users/", include(router.urls))
]


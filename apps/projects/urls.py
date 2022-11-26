from django.urls import path, include
from rest_framework import routers

from . import api

router = routers.DefaultRouter()
router.register("Category", api.CategoryViewSet)
router.register("Project", api.ProjectViewSet)
router.register("Donant", api.DonantViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls)),
]

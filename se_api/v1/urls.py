from django.urls import path, include
from django.contrib.auth import get_user_model
from rest_framework import routers, serializers, viewsets

from se_core.models.seekat import Seekat
from se_api.v1.views.seekat import SeekatViewSet

router = routers.DefaultRouter()
router.register(r'seekats', SeekatViewSet)

urlpatterns = [
    path('', include(router.urls)),
    ]

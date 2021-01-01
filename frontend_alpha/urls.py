from django.contrib import admin
from django.urls import include, path

from frontend_alpha.views import ProfileView

app_name = 'frontend_alpha'

urlpatterns = [
    path('profile/<int:id>/', ProfileView.as_view(), name="profile"),
]

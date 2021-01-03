from django.contrib import admin
from django.urls import include, path

from frontend_alpha.views import LoginView
from frontend_alpha.views import LogoutView
from frontend_alpha.views import ProfileView
from frontend_alpha.views import SignUpView
from frontend_alpha.views import SignUpDetailsView

app_name = 'frontend_alpha'

urlpatterns = [
    path('profile/<int:seeker_id>/', ProfileView.as_view(), name="profile"),
    path('profile/<str:seeker_id>/', ProfileView.as_view(), name="profile"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('login/', LoginView.as_view(), name="login"),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('signup-details/', SignUpDetailsView.as_view(), name="signup-details"),
]

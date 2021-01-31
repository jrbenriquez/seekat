from django.urls import include, path

urlpatterns = [
    path('v1/', include('se_api.v1.urls'))
        ]

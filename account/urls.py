from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from . import views

urlpatterns = [
    path('api-jwt-auth/', obtain_jwt_token),
    path('refresh_jwt_token/', refresh_jwt_token),
    path('verify_jwt_token/', verify_jwt_token),
    path('join', views.join)
]
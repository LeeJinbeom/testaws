from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('students', views.StudentViewSet)

urlpatterns = [
    path('test/<pk>', views.Test),
    path('', include(router.urls))
    #path('students/', views.StudentView.as_view()),
    #path('students/<int:pk>', views.StudentDetailView.as_view())
    #path('students/<int:pk>', views.StudentDetailView)
]

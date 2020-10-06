from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('todogroup', views.TodoGroupViewSet)
router.register('todo', views.TodoViewSet)
router.register('favouritegroup', views.FavouriteGroupViewSet)
router.register('favourite', views.FavouriteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('test', views.Test)
]

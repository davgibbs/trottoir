from rest_framework.routers import DefaultRouter

from . import views


devices_router = DefaultRouter(trailing_slash=False)
devices_router.register(r'devices', views.DevicesViewSet)
urlpatterns = devices_router.urls

from django.conf.urls import url
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


urlpatterns = [
    path('', views.app, name='app'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^update-control-state$', views.update_state)
]

controls_router = DefaultRouter(trailing_slash=False)
controls_router.register(r'controls', views.ControlsViewSet)
urlpatterns += controls_router.urls


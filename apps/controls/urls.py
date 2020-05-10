from django.conf.urls import url
from django.urls import path, include

from controls import views

urlpatterns = [
    path('', views.app, name='app'),
    url(r'^accounts/', include('allauth.urls')),
]

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='index'),
    url(r'^battle/', views.battleGroup, name='battle'),
    url(r'^prueba/', views.prueba, name='prueba')
]
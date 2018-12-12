from django.conf.urls import url
from . import views

app_name = "marvel"

urlpatterns = [
    url(r'^$', views.homepage, name='index'),
    url(r'^battle/', views.battleGroup, name='battle'),
    url(r'^prueba/', views.prueba, name='prueba'),
    #url(r'^eventos/', views.eventos, name='eventos'),
    url(r'^search', views.search, name='search')
]
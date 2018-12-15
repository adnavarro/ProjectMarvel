from django.conf.urls import url
from . import views

app_name = "marvel"

urlpatterns = [
    url(r'^$', views.homepage, name='index'),
    url(r'^battle/', views.battleGroup, name='battle'),
    url(r'^eventos/', views.eventos, name='eventos'),
    url(r'^prueba2/', views.prueba2, name='prueba2'),
    url(r'^testing/', views.testing, name='testing'),
    #url(r'^eventos/', views.eventos, name='eventos'),getPerson
    url(r'^personInGroup/', views.personInGroup, name='personInGroup'),
    url(r'^getPerson/', views.getPerson, name='getPerson'),
    url(r'^search/', views.search, name='search'),
    url(r'^insertEvento/', views.insertEvento, name='insertEvento'),
    url(r'^autoCompleteLugar/', views.autoCompleteLugar, name='autoCompleteLugar')  
]
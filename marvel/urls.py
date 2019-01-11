from django.conf.urls import url
from . import views

app_name = "marvel"

urlpatterns = [
    url(r'^$', views.homepage, name='index'),
    url(r'^battle/', views.battleGroup, name='battle'),
    url(r'^eventos/', views.eventos, name='eventos'),
    url(r'^prueba2/', views.prueba2, name='prueba2'),
    url(r'^testing/', views.testing, name='testing'),
    url(r'^getInscrit/', views.getInscrit, name='getInscrit'),
    url(r'^regPerson/', views.regPerson, name='regPerson'),
    url(r'^regHabili/', views.regHabili, name='regHabili'),
    url(r'^regRel/', views.regRel, name='regRel'), 
    url(r'^personInGroup/', views.personInGroup, name='personInGroup'),
    url(r'^getPerson/', views.getPerson, name='getPerson'),
    url(r'^getIdPerson/', views.getIdPerson, name='getIdPerson'),
    url(r'^combate/', views.combate, name='combate'),
    url(r'^combate_2/', views.combate_2, name='combate_2'),
    url(r'^ganador/', views.ganador, name='ganador'),
    url(r'^consultas/', views.consultas, name='consultas'),
    url(r'^search/', views.search, name='search'),
    url(r'^deletInscri/', views.deletInscri, name='deletInscri'),
    url(r'^insertEvento/', views.insertEvento, name='insertEvento'),
    url(r'^autoCompleteLugar/', views.autoCompleteLugar, name='autoCompleteLugar'),
    url(r'^getCategoria/', views.getCategoria, name='getCategoria')  
]
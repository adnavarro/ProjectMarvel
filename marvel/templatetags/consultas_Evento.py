from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from ..models import *
from django.http import JsonResponse
from datetime import datetime, date, time, timedelta
import json

def buscaLugar(evento):
    nameLugar = ""
    lug = Lugar.objects.get(id = evento.fk_lugar)
    nameLugar = lug.nombre
    return nameLugar

def buscaInscri(evento):
    cadenaIns = ""
    ins = Inscri.objects.filter(fk_evento = evento)
    for inscrito in ins:
        per = Person.objects.get(id = inscrito.fk_person)
        cadenaIns = cadenaIns + per.nombre + " "
    return cadenaIns

def buscaGnador(evento):
    nameGanador = ""
    ins = Inscri.objects.get(fk_evento = evento, campeon = 1)
    per = Person.objects.get(id = ins.fk_person)
    nameGanador = per.nombre
    print(nameGanador)
    return nameGanador

def countBattles(evento):
    dat = Combat.objects.all()
    count = 0
    for i in dat:
        if (i.fech >= evento.fech_in) and (i.fech <= evento.fech_fin):
            count+=count
    print(count)
    return(count)

def convertirEnJson_even(listaEventos):
    listaRespuesta = []
    for evento in listaEventos:     
        jsonRespuesta = {
            'id' : int(evento.id),
            'fech_in': evento.fech_in,
            'fech_fin': evento.fech_fin,
            'Duracion': int(evento.dura),
            'Lugar': buscaLugar(evento),
            'Inscritos': buscaInscri(evento),
            'Batallas': countBattles(evento),
            'Ganador': buscaGnador(evento)
        }
        listaRespuesta.append(jsonRespuesta)
    return json.dumps(listaRespuesta)

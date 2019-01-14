from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from ..models import *
from django.http import JsonResponse
from datetime import datetime, date, time, timedelta
import json

def buscaLugar(evento):
    nameLugar = ""
    lug = evento.fk_lugar
    while lug != None:
        nameLugar = nameLugar + lug.nombre
        lug = lug.fk_lugar
        if lug == None:
            break
        nameLugar = nameLugar + ","
    return nameLugar

def buscaInscri(evento):
    cadenaIns = ""
    ins = Inscri.objects.filter(fk_even = evento)
    indice = 1    
    for inscrito in ins:        
        if indice == len(ins):
            cadenaIns = cadenaIns + inscrito.fk_person.nombre  
            break
        else:
            cadenaIns = cadenaIns + inscrito.fk_person.nombre + ", "

    return cadenaIns

def buscaGnador(evento):
    nameGanador = ""
    ins = Inscri.objects.filter(fk_even = evento, campeon = 1)  
    for nombre in ins: 
        nameGanador = nombre.fk_person.nombre   
    return nameGanador

def countBattles(evento):
    combates = Combat.objects.filter(fech__range = [evento.fech_in,evento.fech_fin])
    listaBatallas = []
    for batalla in combates:
        ganador = ""
        if batalla.ganador == 1:
            ganador = batalla.fk_inscri1.fk_person.nombre
        elif batalla.ganador == 2:
            ganador = batalla.fk_inscri2.fk_person.nombre
        else:
            ganador = "Empate"

        datoJson = {
            'fecha':str(batalla.fech),
            'etapa':int(batalla.etp),
            'ganador':ganador,
            'duracion':int(batalla.dura_min),
            'person1':batalla.fk_inscri1.fk_person.nombre,
            'person2':batalla.fk_inscri2.fk_person.nombre
        }   
        listaBatallas.append(datoJson)
    return json.dumps(listaBatallas)

def convertirEnJson_even(listaEventos):
    listaRespuesta = []   

    for evento in listaEventos: 
        print("inicio:",evento.fech_in)
        print("Armando Json")    
        jsonRespuesta = {
            'id' : int(evento.id),
            'fech_in': str(evento.fech_in),
            'fech_fin': str(evento.fech_fin),
            'Duracion': int(evento.dura),
            'Lugar': buscaLugar(evento),
            'Inscritos': buscaInscri(evento),
            'Batallas': countBattles(evento),
            'Ganador': buscaGnador(evento)
        }
        listaRespuesta.append(jsonRespuesta)
    return json.dumps(listaRespuesta)

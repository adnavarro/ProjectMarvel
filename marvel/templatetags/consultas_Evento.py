from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from ..models import *
from django.http import JsonResponse
from datetime import datetime, date, time, timedelta
import json

def convertirEnJson_even(listaEventos):
    listaRespuesta = []
    for evento in listaEventos:     
        jsonRespuesta = {
            'id' : int(evento.id),
            'fech_in': evento.fech_in,
            'fech_fin': evento.fech_fin,
            'Duracion': int(evento.dura)  
        }  
        listaRespuesta.append(jsonRespuesta)
    return json.dumps(listaRespuesta)

//Busca todas las batallas de un evento
def searchBattles(fechaIni):
    try:
        datEven = Even.objects.get(fech_in=fecha)
    except:
        print('El evento no existe')
        return(-1)
    try:
        dat = Combat.objects.all()
    except:
        print('No hay batallas en el evento')
        return(-1)
    for i in dat:
        if (i.fech >= fechaIni) and (i.fech <= datEven.fech_fin):
            try:
                data.append = i
            except:
                 print('Hubo un error al agregar')
    for e in data:
        print(e)
    return(data)

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
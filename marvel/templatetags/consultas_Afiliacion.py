from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from ..models import *
from django.http import JsonResponse
from datetime import datetime, date, time, timedelta
import json

def obtenerLugar_afiliacion(lugar_afil):  
    cadenaLugar = ""        
    lugar = lugar_afil
    while lugar != None:
        cadenaLugar = cadenaLugar + lugar.nombre
        lugar = lugar.fk_lugar
        if lugar == None:
            break
        cadenaLugar = cadenaLugar + ","             
    return cadenaLugar

def obtenerMiembroActivo_afiliacion(afiliacion):  
    cadenaMiembro = "" 
    listaMiembros = PA.objects.filter(fk_afili = afiliacion , status = "Activo")     
    indice = 1
    for miembro in listaMiembros:
      if indice < len(listaMiembros):
        cadenaMiembro = cadenaMiembro + miembro.fk_person.nombre + " (Activo),"
      else:
        cadenaMiembro = cadenaMiembro + miembro.fk_person.nombre + " (Activo)"                
    return cadenaMiembro

def obtenerMiembroInactivo_afiliacion(afiliacion):  
    cadenaMiembro = "" 
    listaMiembros = PA.objects.filter(fk_afili = afiliacion , status = "Inactivo") 
    indice = 1
    for miembro in listaMiembros:
      if indice < len(listaMiembros):
        cadenaMiembro = cadenaMiembro + miembro.fk_person.nombre + " (Inactivo),"
      else:
        cadenaMiembro = cadenaMiembro + miembro.fk_person.nombre + " (Inactivo)"                
    return cadenaMiembro
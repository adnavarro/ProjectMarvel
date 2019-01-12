from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from ..models import *
from django.http import JsonResponse
from datetime import datetime, date, time, timedelta
import json

def checarFullFiltros(personaje,afiliacion,categoria): #SI SE TIENE EL NOMBRE
    if afiliacion != None:     
        resultadosAfili = PA.objects.filter(fk_person = personaje , fk_afili = afiliacion)
        if categoria != None:
            resultadosCateg = CP.objects.filter(fk_person = personaje , fk_catego__in = categoria)  
            if len(resultadosCateg) > 0 and len(resultadosAfili) > 0:                
                return True
        else:
            if len(resultadosAfili) > 0:
                return True
    
    elif categoria != None:
        resultadosCateg = CP.objects.filter(fk_person = personaje , fk_catego__in = categoria)  
        if len(resultadosCateg) > 0:                
            return True    
    return False

def checarAfiliCateg(afiliacion,categoria): #SI SE TIENE SOLO AFILI 
    resultadosAfili = PA.objects.filter(fk_afili__in = afiliacion)
    listaPersonajes = []
    for personaje in resultadosAfili:
        resultadosCateg = CP.objects.filter(fk_person = personaje.fk_person , fk_catego__in = categoria)
        if len(resultadosCateg) > 0:  
            listaPersonajes.append(personaje.fk_person)
    return listaPersonajes

def checarAfili(afiliacion): #SI SE TIENE SOLO AFILI 
    resultadosAfili = PA.objects.filter(fk_afili__in = afiliacion)
    listaPersonajes = []
    for personaje in resultadosAfili:
        listaPersonajes.append(personaje.fk_person)
    return listaPersonajes

def checarCateg(categoria): #SI SE TIENE SOLO Categoria 
    resultadosCateg = CP.objects.filter(fk_catego__in = categoria)
    listaPersonajes = []
    for personaje in resultadosCateg:
        listaPersonajes.append(personaje.fk_person)
    return listaPersonajes
    

#DESCOMPONIENDO INFORMACION--------------------
def obtenerProfesion(personaje):
    cadenaProfesion = "" 
    profesion = PD.objects.filter(fk_person = personaje)
    indice = 1
    for destresa in profesion:
        if len(profesion) > 1 and indice < len(profesion):
            cadenaProfesion = cadenaProfesion + destresa.fk_destr.nombre + ','
        else:
            cadenaProfesion = cadenaProfesion + destresa.fk_destr.nombre
        indice = indice + 1
    return cadenaProfesion

def obtenerLugares(personaje):
    cadenaLugar = ""        
    lugar = personaje.fk_lugar
    while lugar != None:
        cadenaLugar = cadenaLugar + lugar.nombre
        lugar = lugar.fk_lugar
        if lugar == None:
            break
        cadenaLugar = cadenaLugar + ","             
    return cadenaLugar

def obtenerParientes(personaje):
    relaciones = PerNoper.objects.filter(fk_person = personaje , tipo_paren = 'Familia')
    cadenaParientes = ""

    indice = 1
    for pariente in relaciones:
        if pariente.fk_person_rel == None:
            if indice < len(relaciones):
                cadenaParientes = cadenaParientes + pariente.fk_noperson.nombre_real + " " +  pariente.fk_noperson.apellido_real + ","
            else:
                cadenaParientes = cadenaParientes + pariente.fk_noperson.nombre_real + " " +  pariente.fk_noperson.apellido_real 
        else:
            if indice < len(relaciones):
                cadenaParientes = cadenaParientes + pariente.fk_person_rel.nombre + ","
            else:
                cadenaParientes = cadenaParientes + pariente.fk_person_rel.nombre
        indice = indice + 1
    return cadenaParientes

def obtenerAfiliaciones(personaje):
    listaAfili = PA.objects.filter(fk_person = personaje)
    cadenaAfiliaciones = ""
    indice = 1
    for afiliacion in listaAfili:
        if indice < len(listaAfili):
            cadenaAfiliaciones = cadenaAfiliaciones + afiliacion.fk_afili.nombre + " (" + afiliacion.status + "), " 
        else:
            cadenaAfiliaciones = cadenaAfiliaciones + afiliacion.fk_afili.nombre + " (" + afiliacion.status + ")"

        indice = indice + 1

    return cadenaAfiliaciones
def obtenerAltura(personaje):    
    listaParafer = PPar.objects.filter(fk_person = personaje)    
    if len(listaParafer) > 0:
        for altura in listaParafer:
            return int(altura.altur_armor)
    else:
        return int(personaje.altura)

def obtenerPeso(personaje):    
    listaParafer = PPar.objects.filter(fk_person = personaje)    
    if len(listaParafer) > 0:
        for peso in listaParafer:
            return int(peso.peso_armor)
    else:
        return "???"
def obtenerPoderes(personaje):
    cadenaPoder = ""
    listaPoderes = PPod.objects.filter(fk_person = personaje)
    indice = 1
    for poder in listaPoderes:
        if indice < len(listaPoderes):
            cadenaPoder = cadenaPoder + poder.fk_poder.nombre + " ("+poder.fk_poder.descrip+") , "
        else:
            cadenaPoder = cadenaPoder + poder.fk_poder.nombre + " ("+poder.fk_poder.descrip+")"
        indice = indice+1

    return cadenaPoder

def obtenerParafer(personaje):
    listaParafer = PPar.objects.filter(fk_person = personaje)    
    indice = 1
    cadenaParafer = ""
    if len(listaParafer) > 0:
        for parafer in listaParafer:
            if indice < len(listaParafer):
                cadenaParafer = cadenaParafer + parafer.fk_parafer.nombre + ":" + parafer.fk_parafer.descrip + "("+parafer.fk_parafer.tipo+")_"
            else:
                cadenaParafer = cadenaParafer + parafer.fk_parafer.nombre + ":" + parafer.fk_parafer.descrip + "("+parafer.fk_parafer.tipo+")"
    else:
        return ""
    return cadenaParafer

def obtenerAliados(personaje):
    relaciones = PerNoper.objects.filter(fk_person = personaje , tipo_rel = 'Aliado')
    cadenaAliado = ""
    indice = 1
    for aliado in relaciones:
        if aliado.fk_person_rel == None:
            print(aliado.fk_noperson.nombre_real)            
            if indice < len(relaciones):
                cadenaAliado = cadenaAliado + aliado.fk_noperson.nombre_real + " " +  aliado.fk_noperson.apellido_real + ","
            else:
                cadenaAliado = cadenaAliado + aliado.fk_noperson.nombre_real + " " +  aliado.fk_noperson.apellido_real 
        else:
            print(aliado.fk_person_rel.nombre_real)
            if indice < len(relaciones):
                cadenaAliado = cadenaAliado + aliado.fk_person_rel.nombre + ","
            else:
                cadenaAliado = cadenaAliado + aliado.fk_person_rel.nombre
        indice = indice + 1
    return cadenaAliado

def obtenerEnemigos(personaje):
    relaciones = PerNoper.objects.filter(fk_person = personaje , tipo_rel = 'Enemigo')
    cadenaEnemigo = ""
    indice = 1
    for enemigo in relaciones:
        if enemigo.fk_person_rel == None:                       
            if indice < len(relaciones):
                cadenaEnemigo = cadenaEnemigo + enemigo.fk_noperson.nombre_real + " " +  enemigo.fk_noperson.apellido_real + ","
            else:
                cadenaEnemigo = cadenaEnemigo + enemigo.fk_noperson.nombre_real + " " +  enemigo.fk_noperson.apellido_real 
        else:
            
            if indice < len(relaciones):
                cadenaEnemigo = cadenaEnemigo + enemigo.fk_person_rel.nombre + ","
            else:
                cadenaEnemigo = cadenaEnemigo + enemigo.fk_person_rel.nombre
        indice = indice + 1
    return cadenaEnemigo

def obtenerPodere(personaje):
    listaAtrib = Habili.objects.filter(fk_person = personaje)    
    atributos = []
    for atributo in listaAtrib:
        atributos.append(int(atributo.valor))
    
    return atributos


def convertirEnJson(listaPersonajes):
    listaRespuesta = []
    for personaje in listaPersonajes:
        listaHabilidades = obtenerPodere(personaje)
        universo = "" + personaje.fk_univer.nombre        
        jsonRespuesta = {
            'id' : int(personaje.id),
            'nombre' : personaje.nombre,
            'tipo' : personaje.tipo,
            'tipo_iden' : personaje.tipo_iden,
            'genero' : personaje.genero,
            'altura' : int(personaje.altura),
            'altura_arm': obtenerAltura(personaje),
            'peso': obtenerPeso(personaje),
            'color_ojo' : personaje.color_ojo,
            'biografia' : personaje.biografia,
            'nombre_real' : personaje.nombre_real,
            'apellido_real' : personaje.apellido_real,
            'edo_civil' : personaje.edo_civil,
            'color_pelo' : personaje.color_pelo,
            'lugar' : obtenerLugares(personaje),
            'universo' : universo,
            'profesion': obtenerProfesion(personaje),
            'parientes': obtenerParientes(personaje),
            'afiliaciones':obtenerAfiliaciones(personaje),
            'poderes':obtenerPoderes(personaje),
            'parafernalia':obtenerParafer(personaje),
            'aliados':obtenerAliados(personaje),
            'enemigos':obtenerEnemigos(personaje),
            'fuer':listaHabilidades[0],
            'inteligencia':listaHabilidades[1],
            'agilidad':listaHabilidades[2],
            'resistencia':listaHabilidades[3],
            'proyeccion':listaHabilidades[4],
            'habilidad':listaHabilidades[5]      
        }  
        listaRespuesta.append(jsonRespuesta)
    return json.dumps(listaRespuesta)

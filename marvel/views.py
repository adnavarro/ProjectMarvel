from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .templatetags.battles import * 
from django.http import JsonResponse
from datetime import datetime, date, time, timedelta
import json

def homepage(request):
    return render_to_response('index.html')

def testing(request):
    context = {}
    return render (request, 'testing.html', context)

def prueba2(request):
    return render_to_response('prueba2.html')

def battleGroup(request):    
    obj = Person.objects.all() 
    atributo_fue = 'Fuer'   
    for data in obj:
        obj_id = data.id
        obj_nombre = data.nombre
        obj_tipo = data.tipo
        obj_tipo_iden = data.tipo_iden
        obj_genero = data.genero
        obj_altura = data.altura
        obj_color_ojo = data.color_ojo
        obj_biografia = data.biografia
        obj_nombre_real = data.nombre_real
        obj_apellido_real = data.apellido_real
        obj_edo_civil = data.edo_civil
        obj_color_pelo = data.color_pelo
        obj_fk_lugar = data.fk_lugar
        obj_fk_univer = data.fk_univer       
         
        context = {        
            "obj":obj,
            "obj_id":obj_id,
            "obj_nombre":obj_nombre,
            "obj_tipo":obj_tipo,
            "obj_tipo_iden":obj_tipo_iden,
            "obj_genero":obj_genero,
            "obj_altura":obj_altura,
            "obj_color_ojo":obj_color_ojo,
            "obj_biografia":obj_biografia,
            "obj_nombre_real":obj_nombre,
            "obj_apellido_real":obj_apellido_real,
            "obj_edo_civil":obj_edo_civil,
            "obj_color_pelo":obj_color_pelo,
            "obj_fk_lugar":obj_fk_lugar,
            "obj_fk_univer":obj_fk_univer,
            "atributo_fue":atributo_fue            
        }    
    return render(request, 'battles.html', context)
   
#Aqui estoy probando mis validaciones (Esto no ira en el proyecto final)
#OJO: El Html que estoy utilizando se llama prueba (NO BORRAR POR AHORA)

def prueba(request):
    if request.method == "POST":
        Personaje1 = request.POST.get('Personaje1')
        Personaje2 = request.POST.get('Personaje2')
        battleresult = battles.mula1()
        if battleresult == 1:
            return HttpResponse("Gano el personaje 1")
        if battleresult == 2:
            return HttpResponse("Gano el personaje 2")
        if battleresult == 0:
            return HttpResponse("Hubo un empate")
        else:
 
            return HttpResponse("ERROR")
    return render(request, 'prueba.html', {})

#Se debe crear variables dinamicas para ir almacenando los grupos en python
# Hasta que se decida que se quiere comenzar las batallas y guardar todo.

def search(request): #Aca se reciben los datos, por ahora solo los imprimo por consola y devuelvo un json
    idPerson = request.POST.get('fk_person')
    numGrupo = request.POST.get('num_grupo')
    #Primero vemos si el evento 1 esta creado
    print(idPerson)
    print(numGrupo)
    if personValidate(idPerson) > 0 :#Si es 1 el personaje existe
        return HttpResponse("found") #Enviar una señal al frontend de que se paso las pruebas
    else:
        return HttpResponse("person_not_found")

def autoCompleteLugar(request):
    if request.is_ajax:
        palabra = request.GET.get('find')
       
        lugares = Lugar.objects.filter(nombre__icontains = palabra)
        resultado = []
        lugar_json = {}
        for lugar in lugares:
            print
            lugar_json['label'] = lugar.nombre
            lugar_json['value'] = lugar.nombre 
            resultado.append(lugar_json)
        lugar_json = json.dumps(resultado)
    else:
        lugar_json = 'fail'
    mimetype = 'aplication/json'
    print(lugar_json)
    return HttpResponse(lugar_json,mimetype)

def insertEvento(request):
    if request.is_ajax:
        lugar = request.POST.get('lugar','')
        duracion = request.POST.get('duracion','')        
        idLugar = Lugar.objects.get(nombre = lugar)        
        if guardarEvento(idLugar.id,int(duracion)):
            return HttpResponse("listo")
        else:
            return HttpResponse("fallo")
    else:
        return HttpResponse("no ajax")        


"""
def eventos(request):
    if request.method == "POST":
        try:
            numGrupo = request.POST.get('numGrupo')
            idEvento = request.POST.get('idEvento')
            fkPersonaje = request.POST.get('idPersonaje')
        except (None):
            return HttpResponse("ERROR")
        if battles.personValidate(idPersonaje) == 1:
            ins = Inscri(
                id = battles.newValueId(Inscri),
                n_grupo = numGrupo,
                fk_person = fkPersonaje,
                fk_even = idEvento,
            )
            ins.save()
            print("Personaje inscrito")
    return render(request, 'eventos.html', {})"""
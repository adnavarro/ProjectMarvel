from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .templatetags.battles import *
from .templatetags.save_in_database import *
from django.http import JsonResponse
from datetime import datetime, date, time, timedelta
import json

def regPerson(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        tipo = request.POST.get('tipo')
        tipoIden = request.POST.get('tipo_iden')
        genero = request.POST.get('genero')
        altura = request.POST.get('altura')
        ojos = request.POST.get('color_ojo')
        lugar = request.POST.get('lugar')
        universo = request.POST.get('universo')
        biografia = request.POST.get('biografia')

        HttpResponse(IngPerson(nombre, tipo, tipoIden, genero, altura, ojos, lugar, universo, biografia))
        return redirect('http://127.0.0.1:8000/regHabili/')

    return render(request, 'registroPersonaje.html', {})

def regHabili(request):
    if request.method == "POST":
        inteligencia = request.POST.get('inteligencia')
        fuerza = request.POST.get('fuerza')
        velocidad = request.POST.get('velocidad')
        resistencia = request.POST.get('resistencia')
        proyeccion = request.POST.get('proyeccion')
        habilidad = request.POST.get('habilidad')

        HttpResponse(ingHabili(inteligencia, fuerza, velocidad, resistencia, proyeccion, habilidad))
        return redirect('http://127.0.0.1:8000/regRel/')

    return render(request, 'registroHabili.html', {})

def regRel(request):
    if request.method == "POST":
        name = request.POST.get('nombre')
        tip = request.POST.get('tipo')
        fam = request.POST.get('familia')
    return render(request, 'registroRel.html', {})

def eventos(request):
    return render_to_response('eventos.html')

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

#Se debe crear variables dinamicas para ir almacenando los grupos en python
# Hasta que se decida que se quiere comenzar las batallas y guardar todo.

def search(request): #Aca se reciben los datos, por ahora solo los imprimo por consola y devuelvo un json
    idPerson  = int(request.POST.get('fk_person'))
    numGrupo  = int(request.POST.get('num_grupo'))
    numEnvent = int(request.POST.get('fk_even'))
    
    if personValidate(idPerson) == 1: #Si es 1 el personaje existe
        if perGroupValidate(idPerson, numEnvent) == 1: #verifica que el personaje no este en otro grupo
            if relVali(numGrupo, idPerson, numEnvent) == 1:
                return HttpResponse(inscribirPersonaje(numGrupo, idPerson, numEnvent))
            else:
                return HttpResponse("error_per_rel")
        else:
            return HttpResponse("error_per_usado")
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
        idLugar = None
        if int(duracion) > 3:
            return HttpResponse("fallo_duracion")
        if int(duracion) <= 0:
             return HttpResponse("fallo_duracion_min")
        try:
            idLugar = Lugar.objects.get(nombre = lugar)
        except:
            return HttpResponse("fallo_lugar")
        return HttpResponse(guardarEvento(idLugar.id, int(duracion)))
    else:
        return HttpResponse("no ajax")

def getInscrit(request):
    numeroGrupo = request.GET.get("numGrup")
    numeroEvento = request.GET.get("numEvent")
    inscritos = Inscri.objects.filter(n_grupo = numeroGrupo,fk_even = numeroEvento )
    listaPersonaje = []
    longitud = len(inscritos)
    contador = 0
    for personaje in inscritos: 
        if(contador < (longitud-1) ):       
            listaPersonaje.append( str(personaje.fk_person.id) + ",")
        else:
            listaPersonaje.append( str(personaje.fk_person.id))
        contador = contador + 1

    return HttpResponse(listaPersonaje)

def personInGroup(request):
    lista = request.GET.get("lista[]")
    print(lista)
    lista = eval(lista)
    listaPersonaje = []
    for idPer in lista: 
        per = Person.objects.get(id = idPer)     
        listaPersonaje.append(per.nombre+",")
    return HttpResponse(listaPersonaje)

def getPerson(request):
    id_Person = request.GET.get('id_person')
    person = Person.objects.get( id = id_Person)
    nombre_person = person.nombre
    return HttpResponse(nombre_person)

def deletInscri(request):
    idPerson  = int(request.POST.get('fk_person'))
    numGrupo  = int(request.POST.get('num_grupo'))
    numEnvent = int(request.POST.get('fk_even'))
    
    if personValidate(idPerson) == 1: #Si es 1 el personaje existe
        return HttpResponse(inscriDelete(numGrupo, idPerson, numEnvent))       
    else:
        return HttpResponse("person_not_found")
    
def combate(request):#Recibe parametros de ajax para el evento 
    personaje_1 = int(request.GET.get("primerPersonaje"))#Id
    personaje_2 = int(request.GET.get("segundoPersonaje"))
    numeroGrupo = int(request.GET.get("numGrupo"))
    numeroEvento = int(request.GET.get("numEvento"))
    numeroFase =  int(request.GET.get("numFase")) #Numero de la fase actual
    
    return HttpResponse(simularBatallas(personaje_1, personaje_2, numeroEvento, numeroGrupo,numeroFase))

def deletGroup():
    return HttpResponse("success")
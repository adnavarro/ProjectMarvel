from django.shortcuts import render_to_response, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from . import battles

def homepage(request):
    return render_to_response('index.html')

def battleGroup(request):

    obj = Person.objects.all()
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
        "obj_nombre_real":obj_nombre_real,  
        "obj_apellido_real":obj_apellido_real,
        "obj_edo_civil":obj_edo_civil,
        "obj_color_pelo":obj_color_pelo,   
        "obj_fk_lugar":obj_fk_lugar,
        "obj_fk_univer":obj_fk_univer
    }
    return render_to_response('battles.html', context)
#accediendo a los demas datos

#Aqui estoy probando mis validaciones (Esto no ira en el proyecto final)
#OJO: El Html que estoy utilizando se llama prueba (NO BORRAR POR AHORA)
def prueba(request):
    if request.method == "POST":
        Personaje1 = request.POST.get('Personaje1')
        Personaje2 = request.POST.get('Personaje2')

        if battles.mula1() == 1:
            return HttpResponse("Gano el personaje 1")
        if battles.mula1() == 2:
            return HttpResponse("Gano el personaje 2")
        if battles.mula1() == 0:
            return HttpResponse("Hubo un empate")
        else:
            return HttpResponse("ERROR")
    return render(request, 'prueba.html', {})

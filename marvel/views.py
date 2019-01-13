from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .templatetags.battles import *
from .templatetags.consultas_Personaje import *
from .templatetags.consultas_Evento import *
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

        HttpResponse(ingRel(name, tip, fam))
    return render(request, 'registroRel.html', {})

def consultas(request):
    return render_to_response('consultas.html')
    
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

def deletGroup():
    return HttpResponse("success")

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
    
    return HttpResponse(simularBatallas(personaje_1, personaje_2, numeroEvento, numeroGrupo,numeroGrupo,numeroFase))

def combate_2(request):#Recibe parametros de ajax para el evento 
    personaje_1 = (request.GET.get("primerPersonaje"))#Id
    personaje_2 = (request.GET.get("segundoPersonaje"))
    numeroGrupo = (request.GET.get("numGrupo"))
    numeroGrupo2 = (request.GET.get("numGrupo2"))
    numeroEvento = (request.GET.get("numEvento"))
    numeroFase =  (request.GET.get("numFase")) #Numero de la fase actual
    print(personaje_1)
    print(personaje_2)
    print(numeroGrupo)
    print(numeroGrupo2)
    print(numeroEvento)
    print(numeroFase)
    return HttpResponse(simularBatallas(personaje_1, personaje_2, numeroEvento, numeroGrupo,numeroGrupo2,numeroFase))

def ganador(request):#Recibe parametros de ajax para el evento 
    numGrup = int(request.GET.get("numeroGrup"))#Id
    numEven = int(request.GET.get("numeroEven"))
    numFas  = int(request.GET.get("numeroFas"))    
    
    inscrito = Inscri.objects.filter(n_grupo = numGrup, fk_even = numEven)
    marcadorNombres = []
    marcadorCantidad = []

    for personaje in inscrito:
        marcadorNombres.append(personaje.fk_person.nombre)
        marcadorCantidad.append(0) 

    for personaje in inscrito:
        print("Caso de :",personaje.fk_person.nombre)
        combate = Combat.objects.filter(etp = numFas, fk_inscri1 = personaje) 
        if combate != None:       
            if len(combate) > 0:
                for enfrentamiento in combate:                   
                    ganador1 = enfrentamiento.fk_inscri1.fk_person
                    ganador2 = enfrentamiento.fk_inscri2.fk_person
                    if enfrentamiento.ganador == 1: # SI gana el primero
                        contador = 0
                        for nombreMarcador in marcadorNombres:#Aumenta el marcador de los personajes
                            if nombreMarcador == ganador1.nombre:
                                marcadorCantidad[contador] = marcadorCantidad[contador] + 2 
                            else:
                                contador = contador + 1    
                        print("Gano:",ganador1.nombre)
                    if enfrentamiento.ganador == 2: # Si gana el segundo
                        contador = 0
                        for nombreMarcador in marcadorNombres:#Aumenta el marcador de los personajes
                            if nombreMarcador == ganador2.nombre:
                                marcadorCantidad[contador] = marcadorCantidad[contador] + 2
                            else:
                                contador = contador + 1                         
                        print("Gano:",ganador2.nombre)
                    if enfrentamiento.ganador == 0: #Empate-----------------------------
                        contador = 0
                        for nombreMarcador in marcadorNombres:#Aumenta el marcador de los personajes
                            if nombreMarcador == ganador1.nombre:
                                marcadorCantidad[contador] = marcadorCantidad[contador] + 1
                            else:
                                contador = contador + 1
                        contador = 0
                        for nombreMarcador in marcadorNombres:#Aumenta el marcador de los personajes
                            if nombreMarcador == ganador2.nombre:
                                marcadorCantidad[contador] = marcadorCantidad[contador] + 1
                            else:
                                contador = contador + 1                 
        else:
            combate = Combat.objects.filter(etp = numFas, fk_inscri2 = personaje) 
            if combate != None:       
                if len(combate) > 0:
                    for enfrentamiento in combate:                        
                        ganador1 = enfrentamiento.fk_inscri1.fk_person
                        ganador2 = enfrentamiento.fk_inscri2.fk_person
                        if enfrentamiento.ganador == 1:
                            contador = 0
                            for nombreMarcador in marcadorNombres:#Aumenta el marcador de los personajes
                                if nombreMarcador == ganador1.nombre:
                                    marcadorCantidad[contador] = marcadorCantidad[contador] + 2
                                else:
                                    contador = contador + 1 
                            print("Gano:",ganador1.nombre)
                        if enfrentamiento.ganador == 2:
                            contador = 0
                            for nombreMarcador in marcadorNombres:#Aumenta el marcador de los personajes
                                if nombreMarcador == ganador2.nombre:
                                    marcadorCantidad[contador] = marcadorCantidad[contador] + 2
                                else:
                                    contador = contador + 1 
                            print("Gano:",ganador2.nombre)
                        if enfrentamiento.ganador == 0:
                            contador = 0
                            for nombreMarcador in marcadorNombres:#Aumenta el marcador de los personajes
                                if nombreMarcador == ganador1.nombre:
                                    marcadorCantidad[contador] = marcadorCantidad[contador] + 1
                                else:
                                    contador = contador + 1
                            contador = 0
                            for nombreMarcador in marcadorNombres: #Aumenta el marcador de los personajes
                                if nombreMarcador == ganador2.nombre:
                                    marcadorCantidad[contador] = marcadorCantidad[contador] + 1
                                else:
                                    contador = contador + 1 
    
    empateTotal = comprobarEmpate(marcadorCantidad)    
    listaRespuesta = "" 
    if not empateTotal:
        personajeGanador = getPrimerLugar(marcadorNombres,marcadorCantidad)
        segundoLugar = getSegundoLugar(marcadorNombres,marcadorCantidad)
        listaRespuesta = ("1:"+personajeGanador+","+"2:"+segundoLugar)
    else:
        listaRespuesta = "empate"   
    
    return HttpResponse(listaRespuesta)

def comprobarEmpate(marcadorCantidad):
    diferentes = 0
    for contador in range(0,len(marcadorCantidad)):
        if contador != marcadorCantidad.index(max(marcadorCantidad)):
            if marcadorCantidad[ marcadorCantidad.index(max(marcadorCantidad))] == marcadorCantidad[contador]:            
                return True 

        if contador != marcadorCantidad.index(min(marcadorCantidad)):
            if marcadorCantidad[ marcadorCantidad.index(min(marcadorCantidad))] == marcadorCantidad[contador]:            
                return True
               
    return False

def getPrimerLugar(marcadorNombres,marcadorCantidad):
    return marcadorNombres[marcadorCantidad.index(max(marcadorCantidad))]

def getSegundoLugar(marcadorNombres,marcadorCantidad):
    listaDelSegundo = []
    for contador in range(0,len(marcadorCantidad)):
        print(marcadorCantidad[contador])
        if marcadorCantidad[contador] != marcadorCantidad[marcadorCantidad.index(max(marcadorCantidad))]:
            listaDelSegundo.append(marcadorCantidad[contador])
        else:
            listaDelSegundo.append(0)                      
    
    print("Nueva:",listaDelSegundo)
    return getPrimerLugar(marcadorNombres,listaDelSegundo)

def getIdPerson(request):
    lista1 = eval(request.GET.get("nombrePerson1"))
    lista2 = eval(request.GET.get("nombrePerson2"))
    listaPar = []
    listaImpar = []
    
    for indice in range(0,len(lista1)):
        if indice%2 == 0:
            print("Par",indice)
            personaje = Person.objects.filter(nombre = lista1[indice])
            listaPar.append( personaje[0].id ) #Busca el id por el nombre
            personaje = Person.objects.filter(nombre = lista2[indice])
            listaPar.append( personaje[0].id )
        else:
            print("imparpar",indice)
            personaje = Person.objects.filter(nombre = lista1[indice])
            listaImpar.append( personaje[0].id ) #Busca el id por el nombre
            personaje = Person.objects.filter(nombre = lista2[indice])
            listaImpar.append( personaje[0].id )
        indice = indice + 1
   
    contador = 1
    respuesta = ""
    for id in listaPar:
        print(contador)
        if contador == 1:
            respuesta = respuesta  + str(id)                
        else:
            respuesta = respuesta + "-"
            respuesta = respuesta + str(id)            
        contador = contador + 1

    contador = 1
    respuesta = respuesta + ","
    for id in listaImpar:
        if contador == 1:
            respuesta = respuesta + str(id)
        else:
            respuesta = respuesta + "-"
            respuesta = respuesta + str(id)
        contador = contador + 1

    print(respuesta)
    return HttpResponse(respuesta)
#Busquedas --------------------------------------------------------------------------------------------------------------

def getCategoria(request): 
    listaCategoria = Catego.objects.all()
    listaRespuesta = []

    for categ in listaCategoria:       
        listaRespuesta.append(categ.nombre)
    
    respuesta = ""
    contador = 1

    for resp in listaRespuesta:
        if contador == 1:
            respuesta = respuesta + resp
        else:
            respuesta = respuesta + "_"
            respuesta = respuesta + resp
        contador = contador + 1  

    return HttpResponse(respuesta)
#Busqueda del personaje------------------------------------------------------------------------------------
def buscarPersonaje(request):
    v_nombre = request.GET.get("nombre")
    v_afiliacion = request.GET.get("afiliacion")
    v_categoria = request.GET.get("categoria")
    resultadoBusqueda = []

    #VERIFICANDO QUE LOS DATOS ESTEN LLENOS
    if len(v_nombre) > 0: #INICIANDO EN NOMBRE
        if len(v_afiliacion) > 0:
            if len(v_categoria) > 0:
                resultadoPersonaje   = Person.objects.filter(nombre__icontains = v_nombre) 
                resultadoAfiliacion = Afili.objects.filter(nombre__icontains = v_afiliacion)
                resultadoCatego     = Catego.objects.filter(nombre__icontains = v_categoria)
                #RECORRER LISTA DE RESULTADOS PARA LA BUSQUEDA con todas las clausulas
                for personaje in resultadoPersonaje:
                    for afiliacion in resultadoAfiliacion:
                        if checarFullFiltros(personaje,afiliacion,resultadoCatego):
                            resultadoBusqueda.append(personaje)  
                        else:
                            print("Ninguna coincidencia")                               
            else:
                resultadoPersonaje   = Person.objects.filter(nombre__icontains = v_nombre) 
                resultadoAfiliacion  = Afili.objects.filter(nombre__icontains = v_afiliacion)
                for personaje in resultadoPersonaje:
                    for afiliacion in resultadoAfiliacion:
                        if checarFullFiltros(personaje,afiliacion,None):
                            resultadoBusqueda.append(personaje)  
                        else:
                            print("Ninguna coincidencia")                            
        elif len(v_categoria) > 0:
               resultadoPersonaje = Person.objects.filter(nombre__icontains = v_nombre)  #FIN DE INICIO EN NOMBRE
               resultadoCatego     = Catego.objects.filter(nombre__icontains = v_categoria)
               for personaje in resultadoPersonaje:                    
                    if checarFullFiltros(personaje,None,resultadoCatego):
                        resultadoBusqueda.append(personaje)                        
                    else:
                        print("Ninguna coincidencia")
        else:
            resultadoPersonaje = Person.objects.filter(nombre__icontains = v_nombre)
            for personaje in resultadoPersonaje:
                resultadoBusqueda.append(personaje)

    elif len(v_afiliacion) > 0: #INICIANDO EN AFILIACION  
        if len(v_categoria) > 0:
            resultadoAfiliacion  = Afili.objects.filter(nombre__icontains = v_afiliacion) 
            resultadoCatego      = Catego.objects.filter(nombre__icontains = v_categoria)
            resultadoBusqueda = checarAfiliCateg(resultadoAfiliacion,resultadoCatego) 

        else:      
            resultadoAfiliacion  = Afili.objects.filter(nombre__icontains = v_afiliacion) 
            resultadoBusqueda = checarAfili(resultadoAfiliacion) 
    else:
        resultadoCatego = Catego.objects.filter(nombre__icontains = v_categoria) 
        resultadoBusqueda = checarCateg(resultadoCatego)

    return HttpResponse(convertirEnJson(resultadoBusqueda)) #SE ENVIA EL JSON

# evento ----------------------------------------------------------------------------------------------

def buscarEvento(request):
    v_fecha = request.GET.get("fecha")
    hoy = datetime.today()
    v_fecha = hoy.strftime(v_fecha)
    resultadoBusqueda = []
    print(v_fecha)
    resultadoEvento = Even.objects.filter(fech_in = v_fecha)
    for evento in resultadoEvento:
        resultadoBusqueda.append(evento)

    return HttpResponse(convertirEnJson_even(resultadoBusqueda)) #SE ENVIA EL JSON

#Taza de victorias ---------------------------------------------------------------------------------------

def ganadorSupremo(request):
    iden = int("id")
    evento = Even.objects.get(id = iden)
    inscrito = Inscri.objects.filter(fk_even = evento)
    combate = Combat.objects.all()
    arregloGanadores = []
    arregloPuntajes = []
    persona = 0
    for ins in inscrito:
        win = 0
        for com in combate:
            if (com.fech >= evento.fech_in) and (com.fech <= evento.fech_fin):
                if (com.ganador == 1):
                    if(com.fk_inscri1 == ins.id):
                        win+=win
                        persona.arregloPuntajes=win
                        persona.arregloGanadores=ins.id
                elif (com.ganador == 2):
                    if(com.fk_inscri2 == ins.id):
                        win+=win
                        persona.arregloPuntajes=win
                        persona.arregloGanadores=ins.id
        persona+=persona
    win = 0
    for i in arregloPuntajes:
        if (win < i.arregloPuntajes):
            win = i.arregloPuntajes
    dios = win.arregloGanadores
    print(dios)
    return HttpResponse("Creo que asi seria")
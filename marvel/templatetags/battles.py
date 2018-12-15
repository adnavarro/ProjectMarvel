from django.template import Library
from secrets import randbelow
from datetime import datetime, date, time, timedelta
import calendar
from ..models import *

#crea el evento en la base de datos
def guardarEvento(id_lugar,duracion):
    print("procede a crear evento")
    try:
        even = Even.objects.latest('id')
        evenid= even.id + 1
    except:
        evenid=0
    try:
        lug = Lugar.objects.get(id = id_lugar)
        hoy = datetime.today()        
        fechaActual = "%Y-%m-%d"        
        tab_even = Even.objects.all()        
        id_evento = evenid      
        eve = Even( 
            id = id_evento,
            fech_in =  hoy.strftime(fechaActual),
            fech_fin = (hoy + timedelta(days = duracion)).strftime(fechaActual), 
            dura = duracion,
            fk_lugar = lug
            )        
        eve.save()
        return id_evento
    except:        
        return -1

def inscribirPersonaje(ngrupo,fkperson,fkevento):#id,ngrupo,punto,campeon,descrip,fkPerson,fkGrupo
    try:
        inscri = Inscri.objects.latest('id')
        inscrid= inscri.id + 1
    except:
        inscrid=0
    Persona = Person.objects.get(id = fkperson)
    Event = Even.objects.get(id = fkevento)
    try:
        ins = Inscri(
            id = inscrid,
            n_grupo = ngrupo,
            punto_etp1 = 0,
            descrip = "Personaje listo para la batalla",
            fk_person = Persona,
            fk_even = Event
        )
        ins.save()
        return "Personaje guardado"
    except:
        return "Error: No se pudo guardar"

#Valido que existe el personaje
def personValidate(persona):
    try:
        per = Person.objects.get(id = persona)
    except Person.DoesNotExist:
        return(0) #Si retorna 0 significa que el personaje no existe
    return (1)    #Sino el personaje si existe y me retorna 1

#Valido que los personajes no sean Aliados
def etp1Validate(persona, even, ngrupo):
    try:
        ins = Inscri.objects.get(fk_even = even, n_grupo = ngrupo)
    except Inscri.DoesNotExist:
        return (1)
    IdCompa = ins.fk_person
    try:
        PerNoper.objects.get(fk_person = persona, fk_person_rel = IdCompa, tipo_rel = "Aliado")
    except PerNoper.DoesNotExist:
        return (1) #Si retorna 1 los personajes SI pueden pelear
    return (0) #Si retorna 0 los personajes no pueden pelear

#Valido que el personaje no se encuentre en otro grupo
def perGroupValidate(persona, fech):
    try:
        Inscri.objects.get(fk_person=persona, fk_even = fech)
    except Inscri.DoesNotExist:
        return(1)
    print('Este personaje ya se encuentra inscrito en un grupo')
    return(0)

#Valido que la cantidad de inscritos en un grupo sea impar
def groupInscriVal(ngroup, fecha):
    try:
        dat = Even.objects.get(fech_in=fecha)
    except Even.DoesNotExist:
        return(-1)
    ins = Inscri.objects.all()
    cont = 0
    for i in ins:
        if (ins.fk_even == dat.id) and (ins.n_grupo == ngroup):
            cont+=1
    if count%2 != 0 and count != 1:
        return(1)
    else:
        return(0)

#Valido que la cantidad de grupos sea par
def groupValidate(fecha):
    try:
        dat = Even.objects.get(fech_in=fecha)
    except Even.DoesNotExist:
        return(-1)
    ins = Inscri.objects.all()
    op = 0
    cont = 0
    for i in ins:
        if (ins.fk_even == dat.id):
            if ins.n_ngroup != op:
                op = ins.n_ngroup
                cont+=1
    if cont%2 == 0:
        return(1)
    else:
        return(0)
    
#Simulo la etapa1
def mula1():
    winner=randbelow(3) #0: Empate, 1: Gana el personaje 1, 2: Gana el personaje 2
    return (winner)

def newValueId(table): #recordar que cuando se eliminen datos esto no funcionara optimamente
    return len(table)


    

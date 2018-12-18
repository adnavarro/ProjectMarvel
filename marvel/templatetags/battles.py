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
        if inscri != None:
            inscrid= inscri.id + 1
        else:
            inscrid = 0
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
        return "per_save"
    except:
        return "Error: No se pudo guardar"
    
#Borro a los inscritos de un grupo
def groupDelete(ngroup, fk_even):
    try:
        dat = Even.objects.get(id=fk_even)
    except Even.DoesNotExist:
        return(-1) 
    ins = Inscri.objects.filter(n_grupo=ngroup,fk_even= fk_even)  
    try:
     ins.delete()
    except:
            print("No se pudo borrar a los inscritos")
            return(0)
    return(1)

#Borro a un inscrito especifico
def inscriDelete(ngroup, idpersona, fk_even):
    try:
        dat = Even.objects.get(id=fk_even)
    except Even.DoesNotExist:
        return(-1) 
    try:
        det = Person.objects.get(id=idpersona)
    except Person.DoesNotExist:
        return(-1)    
    ins = Inscri.objects.get(n_grupo=ngroup,fk_person=idpersona,fk_even= fk_even)  
    
    try:
        ins.delete()
    except:            
        return(0)
        
    return(1)
    
#Valido que existe el personaje
def personValidate(persona):
    try:
        per = Person.objects.get(id = persona)
    except Person.DoesNotExist:
        return(0) #Si retorna 0 significa que el personaje no existe
    return (1)    #Sino el personaje si existe y me retorna 1

#Valido que los personajes no esten relacionados
def relVali(ngroup,idpersona, fk_even):
    try:
         ins = Inscri.objects.filter(n_grupo=ngroup,fk_even= fk_even)   
    except Inscri.DoesNotExist:
        return (-1)
    for i in ins:
        try:
            data = PerNoper.objects.get(fk_person = idpersona, fk_person_rel = i.fk_person)
            if (data is not None):
                return(0)
        except PerNoper.DoesNotExist:
            print("Este personaje no guarda relación")
    return (1) #Si retorna 1 los personajes pueden pelear

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
def simularBatallas(personaje_1, personaje_2, numeroEvento, numeroGrupo,numeroFase):
    try:
        combate = Combat.objects.latest('id')
        if combate != None:
            combateId = combate.id + 1
        else:
            combateId = 0        
    except:
        combateId =0
    try:        
        lucha1 = Inscri.objects.get(fk_person = personaje_1, fk_even = numeroEvento, n_grupo = numeroGrupo)
        lucha2 = Inscri.objects.get(fk_person = personaje_2, fk_even = numeroEvento, n_grupo = numeroGrupo)
        hoy = datetime.today()
        win = mula()
        fechaActual = "%Y-%m-%d"
        
        bat = Combat(
            id = combateId,
            fech = hoy.strftime(fechaActual),
            etp = 1,
            ganador = win,
            fk_inscri1 = lucha1,
            fk_inscri2 = lucha2,
        )
        bat.save()
        print("Guardado:",bat.fech,"id:",bat.id)
    except:
        return "Hubo un error, no se pudo realizar el combate"
    if win == 0:
        return "Hubo un empate"
    elif win == 1:
        return "Gano el personaje 1"
    elif win == 2:
        return "Gano el personaje 2"
    else:
        return "Gano un zombie"

def mula():
    winner=randbelow(3) #0: Empate, 1: Gana el personaje 1, 2: Gana el personaje 2
    return (winner)

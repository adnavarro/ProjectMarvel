from django.template import Library
from secrets import randbelow
from ..models import *

#Valido que existe el personaje
def personValidate(persona):
    try:
        per = Person.objects.get(id = persona)
    except Person.DoesNotExist:
        return(0) #Si retorna 0 significa que el personaje no existe
    return (1)    #Sino el personaje si existe y me retorna 1

#Valido que los personajes no sean Aliados
def etp1Validate(persona1, persona2):
    try:
        PerNoper.objects.get(fk_person = persona1, fk_person_rel = persona2, tipo_rel = "Aliado")
    except PerNoper.DoesNotExist:
        print("Estos personajes pueden pelear")
        return (1) #Si retorna 1 los personajes pueden pelear
    print("Estos personajes NO pueden pelear")
    return (0) #Si retorna 0 los personajes no pueden pelear

#Valido que el personaje no se encuentre en otro grupo (OJO: MEJORAR)
def perGroupValidate(persona):
    try:
        Inscri.objects.get(fk_person=persona)
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
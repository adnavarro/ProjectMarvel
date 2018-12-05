import random
from .models import *

#Valido que existe el personaje
def personValidate(persona):
    try:
        per = Person.objects.get(id = persona)
    except Person.DoesNotExist:
        print("Personaje no encontrado")
        return(0) #Si retorna 0 significa que el personaje no existe
    print("Personaje encontrado", per.nombre)
    return (1)    #Sino el personaje si existe y me retorna 1

def dstr(persona):
    try:
       Destre = PD.objects.get(fk_person = persona)
    except PD.DoesNotExist:
        print("Este personaje no tiene destrezas porque es un vago")
        return(-1)
    try:
       Resultado = Destr.objects.get(id = Destre.fk_destr)
    except Destr.DoesNotExist:
        print("Error inesperado: debe faltar algo en la BD")
    return (Resultado.id)

#Valido que los personajes no sean Aliados
def etp1Validate(persona1, persona2):
    try:
        PerNoper.objects.get(fk_person = persona1, fk_person_rel = persona2, tipo_rel = "Aliado")
    except PerNoper.DoesNotExist:
        print("Estos personajes pueden pelear")
        return (1) #Si retorna 1 los personajes pueden pelear
    print("Estos personajes NO pueden pelear")
    return (0) #Si retorna 0 los personajes no pueden pelear

#Simulo la etapa1
def mula1():
    winner = random.randint(0, 2) #0: Empate, 1: Gana el personaje 1, 2: Gana el personaje 2
    print(winner) #Retorno en ganador
    return (winner)

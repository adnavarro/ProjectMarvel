import random
from .models import *

#Valido que existe el personaje
def personValidate(persona):
    try:
        per = Person.objects.get(id = persona)
    except Person.DoesNotExist:
        try:
            per = PersonNoCombat.objects.get(id = persona)
        except PersonNoCombat.DoesNotExist:
            print("Personaje no encontrado")
            return(0) #Si retorna 0 significa que el personaje no existe
    print("Personaje encontrado", per.nombre)
    return (1)    #Sino el personaje si existe y me retorna 1

def etp1Validate(persona1, persona2):
    if personValidate(persona1) != 0 and personValidate(persona2) != 0:
        try:
          PerNoper.objects.get(fk_person = persona1, fk_noperson = persona2, tipo_rel = "Aliado")
        except PerNoper.DoesNotExist:
            try:
              PerNoper.objects.get(fk_person = persona1, fk_person_rel = persona2, tipo_rel = "Aliado")
            except PerNoper.DoesNotExist:
                print("Estos personajes pueden pelear")
                return (1)
        print("Estos personajes NO pueden pelear")
        return (0)
    else:
        print("Uno de los personajes no se encuentra en la BD")
        return(-1)

def mula1(persona1, persona2):
    if etp1Validate(persona1, persona2) == 1:
        winner = random.randint(0, 2)
        print(winner)
        return (winner)
    else:
        print("Los personajes introducidos son incorrectos")
        return (-1)
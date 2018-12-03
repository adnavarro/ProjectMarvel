import random
from .models import *

#Valido que existe el personaje
def personValidate (persona):
    try:
        Person.objects.get(id = persona)
    except Person.DoesNotExist:
        return(0) #Si retorna 0 significa que el personaje no existe
    print("Character found!")
    return (1)    #Sino el personaje si existe y me retorna 1

#Valido que existe el personaje no combatiente (Funciona igual que personValidate)
def personNoCombatValidate (persona):
    try:
        PersonNoCombat.objects.get(id = persona)
    except PersonNoCombat.DoesNotExist:
        return (0)
    print("Character found!")
    return (1)

def etp1Validate (persona, personaNoCombate):
    if personValidate(persona) != 0 and personNoCombatValidate(personaNoCombate) != 0:
        try:
            PerNoper.objects.get(fk_person = persona, fk_noperson = personaNoCombate)
        except PerNoper.DoesNotExist:
            print("Estos personajes NO son parientes")
            return (0)
        print("Estos personajes son parientes")
        return (1)

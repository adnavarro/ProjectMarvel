from django.contrib.sessions.backends.db import SessionStore
from django.template import Library
from .. models import *
from datetime import datetime, date, time, timedelta
import calendar
from .battles import * 

register = Library()

@register.simple_tag()
def isEventEmpy():
    eventos = Even.objects.all()
    if len(eventos) > 0:
        return False
    else:
        return True 

def IngPerson(name, tip, tipoIden, gen, altur, eyes, lugar, universo, biografia):
    try:
        lug = Lugar.objects.get(nombre__iexact = lugar)
        uni = Univer.objects.get(nombre__iexact = universo)
    except:
        return "Lugar o Universo incorrectos"
    try:
        even = Person.objects.latest('id')
        evenid= even.id + 1
    except:
        evenid=0
    try:
        pepe = Person(
            id = newValueId(Person),
            nombre = name,
            tipo = tip,
            tipo_iden = tipoIden,
            genero = gen,
            altura = altur,
            color_ojo = eyes,
            fk_lugar = lug,
            fk_univer = uni
        )
        pepe.save()
        return "Personaje agregado"
    except:
        return "Error al insertar el personaje"

def newValueId(table):
    try:
        even = table.objects.latest('id')
        evenid= even.id + 1
    except:
        evenid=0
    return evenid
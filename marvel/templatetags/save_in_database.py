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

def ingHabili(inte, fuer, veloc, resis, proye, habi):
    try:
        fillInt(inte)
        fillFue(fuer)
        fillVel(veloc)
        fillRes(resis)
        fillProy(proye)
        fillHab(habi)
    except:
        return "Error al cargar habilidades"
    return "Habilidades cargadas"

def ingRel(name, tip, fam):
    try:
        Persona = Person.objects.latest('id')
        related = Person.objects.get(nombre__iexact = name)
    except:
        return "Personaje relacionado incorrecto"
    try:
        even = PerNoper.objects.latest('id')
        evenid= even.id + 1
    except:
        evenid=0
    if fam == 1:
        Parien = "Familia"
    else:
        Parien = None
    try:
        re = PerNoper(
            id = evenid,
            tipo_rel = tip,
            tipo_paren = Parien,
            fk_person = Persona,
            fk_person_rel = related
        )
        re.save()
        return "Relacion establecida"
    except:
        return "No se pudo realizar la relacion"

def fillInt(inte):
    try:
        Persona = Person.objects.latest('id')
    except:
        return -1
    try:
        even = Habili.objects.latest('id')
        evenid= even.id + 1
    except:
        evenid=0
    try:
        i = Habili(
            id = evenid,
            nombre = "Int",
            valor = inte,
            fk_person = Persona
        )
        i.save()
    except:
        return -1
    return 1

def fillFue(fuer):
    try:
        Persona = Person.objects.latest('id')
    except:
        return -1
    try:
        even = Habili.objects.latest('id')
        evenid= even.id + 1
    except:
        evenid=0
    try:
        f = Habili(
            id = evenid,
            nombre = "Fuer",
            valor = fuer,
            fk_person = Persona
        )
        f.save()
    except:
        return -1
    return 1

def fillVel(veloc):
    try:
        Persona = Person.objects.latest('id')
    except:
        return -1
    try:
        even = Habili.objects.latest('id')
        evenid= even.id + 1
    except:
        evenid=0
    try:
        v = Habili(
            id = evenid,
            nombre = "Vel",
            valor = veloc,
            fk_person = Persona
        )
        v.save()
    except:
        return -1
    return 1

def fillRes(resis):
    try:
        Persona = Person.objects.latest('id')
    except:
        return -1
    try:
        even = Habili.objects.latest('id')
        evenid= even.id + 1
    except:
        evenid=0
    try:
        r = Habili(
            id = evenid,
            nombre = "Res",
            valor = resis,
            fk_person = Persona
        )
        r.save()
    except:
        return -1
    return 1

def fillProy(proye):
    try:
        Persona = Person.objects.latest('id')
    except:
        return -1
    try:
        even = Habili.objects.latest('id')
        evenid= even.id + 1
    except:
        evenid=0
    try:
        p = Habili(
            id = evenid,
            nombre = "Proy",
            valor = proye,
            fk_person = Persona
        )
        p.save()
    except:
        return -1
    return 1

def fillHab(habi):
    try:
        Persona = Person.objects.latest('id')
    except:
        return -1
    try:
        even = Habili.objects.latest('id')
        evenid= even.id + 1
    except:
        evenid=0
    try:
        h = Habili(
            id = evenid,
            nombre = "Hab",
            valor = habi,
            fk_person = Persona
        )
        h.save()
    except:
        return -1
    return 1

def newValueId(table):
    try:
        even = table.objects.latest('id')
        evenid= even.id + 1
    except:
        evenid=0
    return evenid
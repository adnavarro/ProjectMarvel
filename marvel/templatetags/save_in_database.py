from django.contrib.sessions.backends.db import SessionStore
from django.template import Library
from .. models import *
from datetime import datetime, date, time, timedelta
import calendar
from .battles import * 

register = Library()

@register.simple_tag()
def insertEvent1():    
    lug = Lugar.objects.get(id = 0)
    hoy = datetime.today()
    fechaActual = "%Y-%m-%d"
    tab_even = Even.objects.all()
    id_evento = battles.newValueId(tab_even)
    eve = Even( 
        id = id_evento,
        fech_in =  hoy.strftime(fechaActual),
        fech_fin = (hoy + timedelta(days=3)).strftime(fechaActual), 
        dura = 3,
        fk_lugar = lug
    ) 
    eve.save()
    return  id_evento  #newValueId(evento)

@register.simple_tag()
def insertInscript(num_grup,idPersonaje,idEven):
    """
    tab_inscri = Inscri.objects.all()
    ins = Inscri(
        id = newValueId(tab_inscri),
        n_grupo = num_grup,
        punto_etp1 = 0,
        campeon = None,
        descrip = "nada",
        fk_person = idPersonaje,
        fk_even = idEven
    )    
    ins.save()"""
    print(idPersonaje)
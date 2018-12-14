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
        
@register.simple_tag()
def insertInscript(num_grup,idPersonaje,idEven):
    
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
    ins.save()
    print(idPersonaje)
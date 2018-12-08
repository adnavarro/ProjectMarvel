from django.template import Library
from .. models import *
from datetime import datetime, date, time, timedelta
import calendar

register = Library()

@register.simple_tag()
def insertEvent1():    
    lug = Lugar.objects.get(id = 0)
    hoy = datetime.today()
    fechaActual = "%Y-%m-%d"
    tab_even = Even.objects.all()
    eve = Even( 
        id = newValueId(tab_even),
        fech_in =  hoy.strftime(fechaActual),
        fech_fin = (hoy + timedelta(days=3)).strftime(fechaActual), 
        dura = 3,
        fk_lugar = lug
    ) 
    eve.save()
    return (hoy + timedelta(days=3)).strftime(fechaActual)   #newValueId(evento)

@register.simple_tag()
def insertInscript(num_grup,idPersonaje,idEven):
    tab_inscri = Inscri.objects.all()
    ins = Inscri(
        id = newValueId(tab_inscri),
        n_grupo = num_grup,
        punto_etp1 = 0,
        campeon = null,
        descrip = "nada",
        fk_person = idPersonaje,
        fk_even = idEven
    )    
    ins.save()
    
def newValueId(table): #recordar que cuando se eliminen datos esto no funcionara optimamente
    return len(table)
    

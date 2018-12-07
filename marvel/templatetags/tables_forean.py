from django.template import Library
from .. models import *

register = Library()

@register.simple_tag()
def getProfesion(id_person):
    miProfesionId = PD.objects.filter(fk_person = id_person)
    contador = 0
    resultado = ''
    for profesionId in miProfesionId:            
        if(len(miProfesionId) > 1 ):
            if(contador == 0):
                resultado = profesionId.fk_destr.nombre
                contador = contador + 1
            else:
                resultado = resultado + ', ' + profesionId.fk_destr.nombre
                contador = contador + 1
        else:
            resultado = profesionId.fk_destr.nombre
            contador = contador + 1
    return resultado

@register.simple_tag()
def getHab(id_person,num_atrib):   
    habilidades = Habili.objects.filter(fk_person = id_person) 
    for atributo in habilidades:
        if(atributo.nombre == num_atrib):           
           return int(atributo.valor) 
        
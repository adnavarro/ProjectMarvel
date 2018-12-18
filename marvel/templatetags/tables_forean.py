from django.template import Library
from .. models import *
import json

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

@register.simple_tag()
def getPoder(id_person):
    miPoderId = PPod.objects.filter(fk_person = id_person)    
    resultado = []
    for poderId in miPoderId:          
        resultado.append(poderId.fk_poder.nombre)            
    return resultado

@register.simple_tag()
def getAfili(id_person):
    miAfiliId = PA.objects.filter(fk_person = id_person)    
    resultado = []
    for afiliId in miAfiliId:          
        resultado.append(afiliId.fk_afili.nombre)            
    return resultado

@register.simple_tag()
def getRela (id_person):
    miRelaId = PerNoper.objects.filter(fk_person = id_person)    
    resultado = []
    for relaId in miRelaId:
        if relaId.fk_person_rel != None:                 
            personaje = relaId.fk_person_rel
            relacion = relaId.tipo_rel
              
            if relaId.tipo_paren != None:
                resultado.append("F:"+personaje.nombre)
            else:                                   
                resultado.append(relacion[0]+":"+personaje.nombre)                                 
            
        
        if relaId.fk_noperson !=  None:
            personaje = relaId.fk_noperson
            relacion = relaId.tipo_rel              
            if relaId.tipo_paren != None:
                resultado.append("F:"+personaje.nombre_real+" "+personaje.apellido_real)
            else:                                   
                resultado.append(relacion[0]+":"+personaje.nombre_real+" "+personaje.apellido_real)

    return resultado
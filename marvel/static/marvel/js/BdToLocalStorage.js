var numero_personaje = 0;
function guardarPersonaje(nombre,apellido,identidad,profesion,lugarN,edoCivil,altura,peso,ojos){
    datos = {
        nombre:nombre,
        apellido:""+apellido,
        profesion:""+profesion,
        lugarN:""+lugarN,
        edoCivil:""+edoCivil,
        altura:""+altura,
        peso:""+peso,
        ojos:""+ojos
    };
    localStorage.setItem('Personaje_'+numero_personaje,datos);
    numero_personaje++;    
}
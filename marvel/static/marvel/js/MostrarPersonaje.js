function vaciarInfo(){
    $("#nombre_person").remove();
    $("#nombre_real_person").remove();
    $("#identidad_person").remove();
    $("#profesion_person").remove();
    $("#lug_nac_person").remove();
    $("#ed_civ_person").remove();
    $("#altura_person").remove();
    $("#peso_person").remove();
    $("#ojos_person").remove();

}
function verDatos(nombre,
    nombre_real,
    identidad,
    profesion,
    lugarN,
    edoCivil,
    altura,
    peso,
    ojos,biografia,sexo,rol){
    function generoFunc(){if(sexo === 'M'){ $("#imagen_heroe_ruta").attr("src","../../static/marvel/img/HeroePerfil.png"); return "Masculino"; }else{ $("#imagen_heroe_ruta").attr("src","../../static/marvel/img/HeroePerfil2.png"); return "Femenino";}}
    function identidadFunc(){if(identidad === 'D') return "Desconocida"; else return "Conocida";}
    function rolFunc(){if (rol === 'H') return "Heroe"; else if (rol === 'V') return "Villano"; else return "Anti-Heroe";}
    $("#nombre_person").html(
    '<p style="margin:-1.5% 0;" ><font SIZE=2>Nombre original: '+nombre+'</font></p>'+
    ' <hr style="margin:-1% 0;"></hr>'
    );
    $("#nombre_real_person").html(
    '<p style="margin:-1.5% 0;"><font SIZE=2>Nombre Real: '+ nombre_real +'</font></p>'+
    ' <hr style="margin:-1% 0;"></hr>'
    );
    $("#identidad_person").html(
    '<p style="margin:-1.5% 0;" ><font SIZE=2>Identidad: '+ identidadFunc() +'</font></p>'+
    ' <hr style="margin:-1% 0;"></hr>'
    );
    $("#sexo_person").html(
    '<p style="margin:-1.5% 0;" ><font SIZE=2>Genero: '+ generoFunc()  +'</font></p>'+
    ' <hr style="margin:-1% 0;"></hr>'
    );
    $("#rol_person").html(
    '<p style="margin:-1.5% 0;" ><font SIZE=2>Rol: '+ rolFunc() +'</font></p>'+
    ' <hr style="margin:-1% 0;"></hr>'
    );
    $("#profesion_person").html(
    '<p style="margin:-1.5% 0;" ><font SIZE=2>Profesion: '+ profesion +'</font></p>'+
    ' <hr style="margin:-1% 0;"></hr>'
    );
    $("#lug_nac_person").html(
    '<p style="margin:-1.5% 0;" ><font SIZE=2>Lugar de nacimiento: '+ lugarN +'</font></p>'+
    ' <hr style="margin:-1% 0;"></hr>'
    );
    $("#ed_civ_person").html(
    '<p style="margin:-1.5% 0;" ><font SIZE=2>Estado civil: '+ edoCivil +'</font></p>'+
    ' <hr style="margin:-1% 0;"></hr>'
    );
    $("#altura_person").html(
    '<p style="margin:-1.5% 0;" ><font SIZE=2>Altura: '+ altura +'</font></p>'+
    ' <hr style="margin:-1% 0;"></hr>'
    );
    $("#peso_person").html(
    '<p style="margin:-1.5% 0;" ><font SIZE=2>Peso: '+ peso +'</font></p>'+
    ' <hr style="margin:-1% 0;"></hr>'
    );
    $("#ojos_person").html(
    '<p style="margin:-1.5% 0;" ><font SIZE=2>Color de ojos: '+ ojos +'</font></p>'+
    ' <hr style="margin:-1% 0;"></hr>'
    );
    
    $("#contenido_biografia").html(
        '<p>'+ biografia +'</p>'        
    );
}




var idPersonajeActual = -1;
var arregloDeIdPorGrupo = [];
var grupoCreado = {
    nombre:'',
    integrante:''
};

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
function llenarHabilida(cantidad,id,nombre){
    atributo = ''
    for (contador = 0; contador < cantidad; contador++) {
        if(contador < 1){
            atributo += '<td class="table-info"></td>';
        }else if(contador < 2){
            atributo += '<td class="table-primary"></td>';
        }else if(contador < 3){
            atributo += '<td class="table-success"></td>';
        }else if(contador < 5){
            atributo += '<td class="table-warning"></td>';
        }else if (contador < 8){
            atributo += '<td class="table-danger"></td>';
        }
                
    }
    $("#"+id).html(
        '<th scope="row">'+nombre+'</th>'+ atributo               
    );    
}
function llenarAtributo(fuer,inte,agil,resis,proyect,habC){
    llenarHabilida(fuer,'fuer','Fuerza');
    llenarHabilida(inte,'intel','Inteligencia');
    llenarHabilida(agil,'agil','Agilidad');
    llenarHabilida(resis,'resi','Resistencia');
    llenarHabilida(proyect,'proy_en','Proyeccion de Energia');
    llenarHabilida(habC,'hab_comb','Habilidad de combate');     
}
function verDatos(nombre,
    nombre_real,
    identidad,
    profesion,
    lugarN,
    edoCivil,
    altura,
    peso,
    ojos,biografia,sexo,rol,
    fuer,inte,agil,resi,proy,hab,id){
        
    llenarAtributo(fuer,inte,agil,resi,proy,hab);
    
    function generoFunc(){if(sexo === 'M'){ $("#imagen_heroe_ruta").attr("src","../../static/marvel/img/HeroePerfil.png"); return "Masculino"; }else{ $("#imagen_heroe_ruta").attr("src","../../static/marvel/img/HeroePerfil2.png"); return "Femenino";}}
    function identidadFunc(){if(identidad === 'D') return "Desconocida"; else return "Conocida";}
    function rolFunc(){if (rol === 'H') return "Heroe"; else if (rol === 'V') return "Villano"; else return "Anti-Heroe";}
    function edoCivilFunc(edo) { if(edo === "S") return "Soltero"; else return "Casado"; }

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
    '<p style="margin:-1.5% 0;" ><font SIZE=2>Estado civil: '+ edoCivilFunc(edoCivil) +'</font></p>'+
    ' <hr style="margin:-1% 0;"></hr>'
    );
    $("#altura_person").html(
    '<p style="margin:-1.5% 0;" ><font SIZE=2>Altura: '+ altura +'cm</font></p>'+
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
    verificarFocusGrupo(id); 
}

function verificarFocusGrupo(id){
    if(!sessionStorage.getItem("actualGroup")){
        $("#Añadir_Heroe").css("display","none");
        idPersonajeActual = -1;
    }else{
        $("#Añadir_Heroe").css("display","block");
        idPersonajeActual = id;  
        if(!sessionStorage.getItem("miembros_"+sessionStorage.getItem("actualGroup"))) {
            arregloDeIdPorGrupo = [];
            alert("Vacio");           
        }else{
            if(sessionStorage.getItem("miembros_"+sessionStorage.getItem("actualGroup")).length > 0)
            arregloDeIdPorGrupo  = JSON.parse(sessionStorage.getItem("miembros_"+sessionStorage.getItem("actualGroup")));
            else
                arregloDeIdPorGrupo = [];
        }                     
    }      
}

function agegarPersonajeGrupo(){
    operacionExitosa = true;
    if(arregloDeIdPorGrupo.length > 0){
        arregloDeIdPorGrupo.forEach(idPersonaj => {
            if(idPersonaj === idPersonajeActual){
                alert("Personaje agregado");
                operacionExitosa = false;
            }
        });
        if(operacionExitosa){
            arregloDeIdPorGrupo.push(idPersonajeActual);
            almacenarDatosStorage(sessionStorage.getItem("actualGroup"),arregloDeIdPorGrupo); 
        }
    }else{
        arregloDeIdPorGrupo.push(idPersonajeActual);
        almacenarDatosStorage(sessionStorage.getItem("actualGroup"),arregloDeIdPorGrupo); 
    }   
}
function almacenarDatosStorage(nombreGrupo,listaMiembros) {  
    sessionStorage.setItem("miembros_"+nombreGrupo,JSON.stringify(listaMiembros));
}




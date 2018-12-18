
var idPersonajeActual = -1;
var arregloDeIdPorGrupo = [];

function getPersonaje(){
    $.ajax({
        url: "/getPerson/",
        type: "GET",
        data:{ 
            id_person:idPersonajeActual,              
        },
        success:function(respuesta){
            
            $("#scroll_heroe").append(
                '<div class="list-group"> '+         
                '<button type="button" class="list-group-item list-group-item-action">'+respuesta+'</button>'+ 
                '</div>' 
            );            
        },
        error:function(error){
            $("#scroll_heroe").append(
                '<div class="list-group"> '+         
                '<button type="button" class="list-group-item list-group-item-action">'+"personaje"+'</button>'+ 
                '</div>' 
            ); 
        }    
    });
}
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
    fuer,inte,agil,resi,proy,hab,id,
    listaPoderes,listaAfili,listaRelaciones){
    llenarRelaciones(listaRelaciones);    
    llenarAtributo(fuer,inte,agil,resi,proy,hab);
    llenarPoderes(listaPoderes);
    llenarAfiliaciones(listaAfili);
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
        $('#Eliminar_Heroe').css('display','none');                
        $("#Añadir_Heroe").css("display","none");
        idPersonajeActual = -1;
    }else{
        idPersonajeActual = id; 
        encontrado = false;
        nombreGrupo = sessionStorage.getItem("actualGroup");

        if(sessionStorage.getItem(nombreGrupo)){ //Si el grupo no esta vacio
            integrantes = JSON.parse(sessionStorage.getItem(nombreGrupo));
            if(integrantes.length > 0){
                arregloDeIdPorGrupo = integrantes;
                integrantes.forEach(function(element){
                    if(element === idPersonajeActual){
                        encontrado = true;                                    
                    }
                });
            }else{
                arregloDeIdPorGrupo = [];
            }            
        }else{
            arregloDeIdPorGrupo = [];
        }        
        if(!encontrado){
            $("#Eliminar_Heroe").css("display","none");
            $("#Añadir_Heroe").css("display","block");
        }else if (encontrado){            
            $('#Eliminar_Heroe').css('display','block');
            $("#Añadir_Heroe").css("display","none");
        }  

        //condicion si esta en un grupo 
                          
    }      
}

function agegarPersonajeGrupo(token){//Se usa una lista que se vaciara si se cambia de focus en el grupo
    operacionExitosa = true; //
    personajeEnUso = false;    
    $.ajax({
        url: "/search/",
        type: "POST",
        data:{ 
              fk_person:idPersonajeActual,
              num_grupo:sessionStorage.getItem("numeroGrupo"),
              fk_even:sessionStorage.getItem("eventoActual"),
              csrfmiddlewaretoken: token
            },            
        success: function(respuesta){
            if(respuesta === "per_save"){
                alert("Personaje guardado");
                arregloDeIdPorGrupo.push(idPersonajeActual);
                sessionStorage.setItem(sessionStorage.getItem("actualGroup"),JSON.stringify(arregloDeIdPorGrupo));
                $('#Eliminar_Heroe').css('display','block');
                $('#Añadir_Heroe').css('display','none');
                getPersonaje();                
            }else if(respuesta === "error_per_usado"){
                alert("El personaje ya esta en un grupo");
            }else if("error_per_rel"){
                alert("no pueden haber personajes con alguna relacion en un mismo grupo");
            }                        
        },error:function(data){
            alert("error");            
        }
      });   
}

function eliminarPersonajeGrupo(token){//Se usa una lista que se vaciara si se cambia de focus en el grupo
    operacionExitosa = true; //
    personajeEnUso = false;    
    $.ajax({
        url: "/deletInscri/",
        type: "POST",
        data:{ 
              fk_person:idPersonajeActual,
              num_grupo:sessionStorage.getItem("numeroGrupo"),
              fk_even:sessionStorage.getItem("eventoActual"),
              csrfmiddlewaretoken: token
            },            
        success: function(respuesta){
            if(respuesta === "1"){
                alert("Personaje Eliminado");
                arregloDeIdPorGrupo.pop(idPersonajeActual);
                sessionStorage.setItem(sessionStorage.getItem("actualGroup"),JSON.stringify(arregloDeIdPorGrupo));
                $('#Eliminar_Heroe').css('display','none');
                $('#Añadir_Heroe').css('display','block');
                integrantesRestantes = JSON.parse(sessionStorage.getItem( sessionStorage.getItem("actualGroup")));
                if(integrantesRestantes.length > 0)
                    focusGrupos(sessionStorage.getItem("actualGroup"),sessionStorage.getItem("numeroGrupo"),token)
                else{
                    sessionStorage.removeItem(sessionStorage.getItem("actualGroup"));
                    focusGrupos(sessionStorage.getItem("actualGroup"),sessionStorage.getItem("numeroGrupo"),token);
                }               
            }
            else{
                alert("no se pudo eliminar el personaje");
            }                        
        },error:function(data){
            alert("error");            
        }
      });   
}

function llenarPoderes(listaPoder){     
    dato = tokenizarDato(listaPoder);
    $("#lista_poderes").html('<ul class="list-goup"><li class="list">  </li></ul>');   
    
    for(indice = 0;indice < dato.length; indice++) {
        $("#lista_poderes li").append(        
            '<button type="button" class="list-group-item list-group-item-info" onclick="mostrarPoder('+"'"+dato[indice]+"'"+','+"'Descripcion del poder'"+');" style="width:100%; height: 20px; margin: 0; padding: 0; text-align: center;"> <b>'+"Poder: "+(indice+1)+'</b> </button>'               
        );       
     }   
}
function llenarAfiliaciones(listaAfili){
    dato = tokenizarDato(listaAfili);
    $("#lista_afiliaciones").html('<ul class="list-goup"><li class="list">  </li></ul>');   
    
    for(indice = 0;indice < dato.length; indice++) {
        if(dato[indice].length > 0){
            $("#lista_afiliaciones li").append(        
                '<button type="button" class="list-group-item list-group-item-info"  style="width:100%; height: 20px; margin: 0; padding: 0; text-align: center;"> <b>'+dato[indice]+'</b> </button>'               
            ); 
        }              
     }   
}
function aliaOEnem(data){
    if(data.indexOf("A:") > -1){
        arreglo = data.split(":");
        personaje = arreglo[1];
        $("#lista_relaciones li").append(        
            '<button type="button" class="list-group-item list-group-item-success"  style="width:100%; height: 20px; margin: 0; padding: 0; text-align: center;"> <b>'+personaje+'</b> </button>'               
        ); 
    }else if(data.indexOf("E:") > -1){
        arreglo = data.split(":");
        personaje = arreglo[1];
        $("#lista_relaciones li").append(        
            '<button type="button" class="list-group-item list-group-item-danger"  style="width:100%; height: 20px; margin: 0; padding: 0; text-align: center;"> <b>'+personaje+'</b> </button>'               
        ); 
    }else if(data.indexOf("F:") > -1){
        arreglo = data.split(":");
        personaje = arreglo[1];
        $("#lista_relaciones li").append(        
            '<button type="button" class="list-group-item list-group-item-info"  style="width:100%; height: 20px; margin: 0; padding: 0; text-align: center;"> <b>'+personaje+'</b> </button>'               
        );   
    }
}
function llenarRelaciones(listaRelaciones){
    dato = tokenizarDato(listaRelaciones);
    $("#lista_relaciones").html('<ul class="list-goup"><li class="list">  </li></ul>');   
    
    for(indice = 0;indice < dato.length; indice++) {
        aliaOEnem(dato[indice]);             
     }   
}
function tokenizarDato(cadena){
    inicio = cadena.indexOf("[") + 1;
    fin = cadena.indexOf("]");
    subCadena = cadena.substring(inicio, fin);
    array = subCadena.split(",");
    resultado = [];
    for(var indice = 0; indice < array.length;indice++){
        subCadena = array[indice].replace(/'/g,'');
        resultado.push(subCadena);
    } 
    return resultado;
}


function llenarAlias(){

}
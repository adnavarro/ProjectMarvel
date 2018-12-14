var lista_grupos = []
var numero_grupo = 1;

function cargarListaGrupos() { 
    if(!sessionStorage.getItem("lista_grupos")){
        console.log("No hay grupos");
    }  else{
        sessionStorage.removeItem('actualGroup');
        lista_grupos = JSON.parse(sessionStorage.getItem("lista_grupos"));
        
        lista_grupos.forEach(function(grupo) {
            $( "#agregar_nuevo_grupo").append(    
                ' <li class="list-group-item grupo-combate" id="grupo_'+numero_grupo+'">'+
                     '<div class="row" style="color:black; padding:0;margin:0; width:100%">'+
                         '<div onclick="focusGrupo('+"'"+grupo+"'"+','+numero_grupo+');" style="overflow:auto;width: 80%">'+
                             grupo+
                         '</div>'+
                         '<div>'+
                             '<button type="button" class="btn btn-danger" onclick="quitarElemento('+"'grupo_"+ numero_grupo+"','"+grupo+"'"+');">X</button>'+
                         '</div> '+
                     '</div>'+
                '</li>'
            );
            numero_grupo++;    
        });
    }
}

function agregarNuevoGrupo(nombre_grupo,nombre_elemento){ //Agrega la etiqueta del grupo 
    if(lista_grupos.length === 0){
        $( "#"+nombre_grupo ).append(    
            ' <li class="list-group-item grupo-combate" id="grupo_'+numero_grupo+'">'+
                 '<div class="row" style="color:black; padding:0;margin:0; width:100%">'+
                     '<div onclick="focusGrupo('+"'"+nombre_elemento+"'"+','+numero_grupo+');" style="overflow:auto;width: 80%">'+
                         nombre_elemento+
                     '</div>'+
                     '<div>'+
                         '<button type="button" class="btn btn-danger" onclick="quitarElemento('+"'grupo_"+ numero_grupo+"','"+nombre_elemento+"'"+');">X</button>'+
                     '</div> '+
                 '</div>'+
             '</li>'
        );        
        lista_grupos.push(nombre_elemento);
        sessionStorage.setItem("lista_grupos",JSON.stringify(lista_grupos)); 
        numero_grupo++;   
    }else if(lista_grupos.length > 0){
        operacionExitosa = true;

        lista_grupos.forEach(function(grupo){
            if(grupo === nombre_elemento)
               operacionExitosa = false;            
        });
        if(operacionExitosa === true){
            $( "#"+nombre_grupo ).append(    
            ' <li class="list-group-item grupo-combate" id="grupo_'+numero_grupo+'">'+
                '<div class="row" style="color:black; padding:0;margin:0; width:100%">'+
                    '<div onclick="focusGrupo('+"'"+nombre_elemento+"'"+','+numero_grupo+');" style="overflow:auto;width: 80%">'+
                        nombre_elemento+
                    '</div>'+
                    '<div>'+
                        '<button type="button" class="btn btn-danger" onclick="quitarElemento('+"'grupo_"+ numero_grupo+"','"+nombre_elemento+"'"+');">X</button>'+
                    '</div> '+
                '</div>'+
            '</li>'
        );
            lista_grupos.push(nombre_elemento);
            sessionStorage.setItem("lista_grupos",JSON.stringify(lista_grupos));
            numero_grupo++; 
        }else{
            alert("Grupo repetido");
        }
    }    
}
function quitarElemento(id_elemento,nombre_elemento){ //Elimina la etiqueta
    lista_grupos.splice( lista_grupos.indexOf(nombre_elemento), 1 );   
    
    
    //JSON.parse(sessionStorage.getItem("personajes_usados"));
    //JSON.parse(sessionStorage.getItem("miembros_"+nombre_elemento));
    
    sessionStorage.removeItem("miembros_"+nombre_elemento);
    
    $("#"+id_elemento).remove();
    if(sessionStorage.getItem('actualGroup') === nombre_elemento ){
        $('#palabra_nombre').remove();
        sessionStorage.removeItem('actualGroup');
    }
    if(lista_grupos.length > 0)
        sessionStorage.setItem("lista_grupos",JSON.stringify(lista_grupos));
    else
        sessionStorage.removeItem("lista_grupos");
        
}
function focusGrupo(nombre_elemento,numero){ //Hace focus a la etiqueta seleccionada
    alert(numero);
    sessionStorage.removeItem('actualGroup');
    sessionStorage.setItem('numeroGrupo',numero);
    sessionStorage.setItem('actualGroup',nombre_elemento);
    $('#palabra_nombre').remove();
    $('#nombre_del_grupo').append(
        '<center id="palabra_nombre" >'+nombre_elemento+'</center>'
    );
}
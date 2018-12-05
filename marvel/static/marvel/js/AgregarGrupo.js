
var numero_grupo = 0;
function agregarNuevo(nombre_grupo,nombre_elemento){ //Agrega la etiqueta del grupo   
    $( "#"+nombre_grupo ).append(    
        ' <li class="list-group-item grupo-combate" id="grupo_'+numero_grupo+'">'+
             '<div class="row" style="color:black; padding:0;margin:0; width:100%">'+
                 '<div onclick="focusGrupo('+"'"+nombre_elemento+"'"+');" style="overflow:auto;width: 80%">'+
                     nombre_elemento+
                 '</div>'+
                 '<div>'+
                     '<button type="button" class="btn btn-danger" onclick="quitarElemento('+"'grupo_"+ numero_grupo+"','"+nombre_elemento+"'"+');">X</button>'+
                 '</div> '+
             '</div>'+
         '</li>'
    );    
    numero_grupo++;    
}
function quitarElemento(id_elemento,nombre_elemento){ //Elimina la etiqueta
    $("#"+id_elemento).remove();
    if(sessionStorage.getItem('actualGroup') === nombre_elemento ){
        $('#palabra_nombre').remove();
        sessionStorage.removeItem('actualGroup');
    }
}
function focusGrupo(nombre_elemento){ //Hace focus a la etiqueta seleccionada
    sessionStorage.removeItem('actualGroup');
    sessionStorage.setItem('actualGroup',nombre_elemento);
    $('#palabra_nombre').remove();
    $('#nombre_del_grupo').append(
        '<center id="palabra_nombre" >'+nombre_elemento+'</center>'
    );
}
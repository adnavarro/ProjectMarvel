
var numero_grupo = 0;
function agregarNuevo(nombre_grupo,nombre_elemento){
    
    $( "#"+nombre_grupo ).append(    
        ' <li class="list-group-item " id="grupo_'+numero_grupo+'">'+
             '<div class="row" style="color:black; padding:0;margin:0; width:100%">'+
                 '<div  style="overflow:auto;width: 80%">'+
                     nombre_elemento+
                 '</div>'+
                 '<div>'+
                     '<button type="button" class="btn btn-danger" onclick="quitarElemento('+"'grupo_"+ numero_grupo+"'"+');">X</button>'+
                 '</div> '+
             '</div>'+
         '</li>'
    );    
    numero_grupo++;    
}
function quitarElemento(id_elemento){
    $("#"+id_elemento).remove();
}
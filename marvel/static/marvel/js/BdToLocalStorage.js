
function sendData(idPersonaje,numGrupo,idEven){
    alert("agregando");
    $("form").html(        
       '<input type="number" name="idPersonaje" style="display:block;" class="form-control" value="'+idPersonaje+'">'+
       '<input type="number" name="idEvento" style="display:block;" class="form-control" value="'+idEven+'">'+
       '<input type="number" name="numGrupo" style="display:block;" class="form-control" value="'+numGrupo+'">'  
    );
    $("form").submit();
}
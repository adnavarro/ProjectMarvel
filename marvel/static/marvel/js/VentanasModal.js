
function crearModalPoder(){
    $("body").append(
    '<div class="modal fade" id="modal_poder" tabindex="-1" role="dialog" aria-labelledby="modal_poder" aria-hidden="true" >'+
    '    <div class="modal-dialog modal-dialog-centered"  role="document">'+
    '      <div class="modal-content" style="border-right:3px solid rgba(145, 152, 252, 0.281);border-left:3px solid rgba(145, 152, 252, 0.281);border-top:3px solid rgba(145, 152, 252, 0.281);border-bottom:3px solid rgba(145, 152, 252, 0.281);background-color: rgb(241, 241, 241);">'+
    '        <div class="modal-header">'+
    '          <h5 class="modal-title" id="modal_titulo_poder">Poder</h5>'+
    '          <button type="button" class="close" data-dismiss="modal" aria-label="Close">'+
    '            <span aria-hidden="true">&times;</span>'+
    '          </button>'+
    '        </div>'+
    '        <div class="modal-body" id="modal_descripcion_poder">'+
    '          Descripcion del poder'+
    '        </div>'+
    '        <div class="modal-footer">'+
    '          <button type="button" class="btn btn-info" data-dismiss="modal">Close</button>'+
    '        </div>'+
    '      </div>'+
    '    </div>'+
    '  </div>'
    );
}
function mostrarPoder(nombrePoder,descripcion){
    $("#modal_titulo_poder").html(nombrePoder);
    $("#modal_descripcion_poder").html(descripcion);
    $('#modal_poder').modal("show");
}


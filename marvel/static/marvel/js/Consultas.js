function listaCategorias(){//getCategoria
  $.ajax({
    url:"/getCategoria/",
    type:"GET",
    data:{ 
      dato:'obtener'
    },
    success: function(respuesta){ 
       listado = [];
       listado = respuesta.split('_');
       
       for(var indice = 0; indice < listado.length; indice ++){
         $('#sel_categ').append(
           "<option>"+listado[indice]+"</option>"
         );
       }      
       
    },
    error: function(respuesta){ alert("Error Busqueda"); }    
  });
}

function crearModalFichaPerson(){
  $("#modal_personaje").html(
    '<div class="modal fade" id="ficha_personaje" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">'+
      '<div class="modal-dialog" role="document">'+
        '<div class="modal-content">'+
          '<div class="modal-header">'+
            '<h5 class="modal-title" id="exampleModalLabel">Ficha de Personaje</h5>              '+
          '</div>'+
          '<div class="modal-body">'+
            '<form>'+
                
              '<div class="row"> <!-- Nombre , nombre real y universo -->'+
                '<div class="col" id="titulo_ficha">'+
                  '<label >Nombre de Heroe - Nombre real (Universo)</label>'+
                '</div>                                '+
              '</div> <!-- Nombre -->'+

              '<div class="form-group" id="biografria_ficha"> <!-- Biografia -->'+
                  '<label for="message-text" class="col-form-label">Biografia:</label>'+
                  '<textarea class="form-control" id="message-text" readonly> Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nihil, illum dolorum animi impedit quae distinctio consequatur consequuntur odio quidem sapiente porro explicabo voluptatibus neque aliquam debitis ad ut laboriosam minus.</textarea>'+
              '</div> <!-- Biografia -->'+
              
              '<!--Datos -->'+
              '<div class="row"> '+
                '<div class="col">'+
                  '<label >Nombre Original:</label>'+
                '</div>'+
                '<div class="col-6" id="nombreOriginal_Ficha">'+
                  '<input class="form-control" value="Nombre" id="nombre-text" readonly>'+
                '</div>                '+
              '</div>   '+
              
              '<div class="row"> '+
                '<div class="col">'+
                  '<label >Nombre Real:</label>'+
                '</div>'+
                '<div class="col-6" id="nombreReal_Ficha">'+
                  '<input class="form-control" value="Nombre" id="nombre-text" readonly>'+
                '</div>                '+
              '</div>'+

              '<div class="row"> '+
                '<div class="col">'+
                  '<label >Identidad:</label>'+
                '</div>'+
                '<div class="col-6" id="identidad_Ficha">'+
                  '<input class="form-control" value="Nombre" id="nombre-text" readonly>'+
                '</div>                '+
              '</div>'+

              '<div class="row"> '+
                '<div class="col">'+
                  '<label >Profesion:</label>'+
                '</div>'+
                '<div class="col-6" id="profesion_Ficha">'+
                  '<input class="form-control" value="Nombre" id="nombre-text" readonly>'+
                '</div>                '+
              '</div>'+

              '<div class="form-group" id="lugarNac_Ficha"> <!-- Lugar nac -->'+
                '<label for="message-text" class="col-form-label">Lugar de nacimiento:</label>'+
                '<textarea class="form-control" id="message-text" readonly> Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nihil, illum dolorum animi impedit quae distinctio consequatur consequuntur odio quidem sapiente porro explicabo voluptatibus neque aliquam debitis ad ut laboriosam minus.</textarea>'+
              '</div> <!-- lugar nac -->'+

              '<div class="row"> '+
                '<div class="col">'+
                  '<label >Estado civil:</label>'+
                '</div>'+
                '<div class="col-6" id="edoCivil_Ficha">'+
                  '<input class="form-control" value="Nombre" id="nombre-text" readonly>'+
                '</div>                '+
              '</div>'+

              '<div class="form-group"> <!-- Parientes -->'+
                '<label for="message-text" class="col-form-label">Parientes conocidos:</label>'+
                '<textarea class="form-control" id="message-text" readonly> Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nihil, illum dolorum animi impedit quae distinctio consequatur consequuntur odio quidem sapiente porro explicabo voluptatibus neque aliquam debitis ad ut laboriosam minus.</textarea>'+
              '</div> <!-- Parientes -->'+

              '<div class="form-group"> <!-- Biografia -->'+
                '<label for="message-text" class="col-form-label">Grupos de Afiliacion:</label>'+
                '<textarea class="form-control" id="message-text" readonly> Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nihil, illum dolorum animi impedit quae distinctio consequatur consequuntur odio quidem sapiente porro explicabo voluptatibus neque aliquam debitis ad ut laboriosam minus.</textarea>'+
              '</div> <!-- Biografia -->'+

              '<div class="row"> <!--Fisico-->'+
                '<div class="col-2">'+
                  '<label >Altura:</label>'+
                '</div>'+
                '<div class="col-2">'+
                  '<input class="form-control" value="0" id="nombre-text" readonly>'+
                '</div> '+
                '<div class="col-2">'+
                  '<input class="form-control" value="0" id="nombre-text" readonly>'+
                '</div> '+

                '<div class="col-2">'+
                  '<label >Peso:</label>'+
                '</div>'+
                '<div class="col-2">'+
                  '<input class="form-control" value="0" id="nombre-text" readonly>'+
                '</div> '+

                '<div class="col-2">'+
                  '<input class="form-control" value="0" id="nombre-text" readonly>'+
                '</div> '+
              '</div> <!--Fisico-->'+

              '<div class="row"> <!--Fisico-->'+
                '<div class="col-2">'+
                  '<label >Ojos:</label>'+
                '</div>'+
                '<div class="col-4">'+
                  '<input class="form-control" value="azul" id="nombre-text" readonly>'+
                '</div>                 '+

                '<div class="col-2">'+
                  '<label >Pelo:</label>'+
                '</div>'+
                '<div class="col-4">'+
                  '<input class="form-control" value="negro" id="nombre-text" readonly>'+
                '</div>                 '+

              '</div> <!--Fisico-->'+

              '<div class="form-group"> <!-- Biografia -->'+
                '<label for="message-text" class="col-form-label">Poderes conocidos:</label>'+
                '<textarea class="form-control" id="message-text" readonly> Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nihil, illum dolorum animi impedit quae distinctio consequatur consequuntur odio quidem sapiente porro explicabo voluptatibus neque aliquam debitis ad ut laboriosam minus.</textarea>'+
              '</div> <!-- Biografia -->'+

              '<div class="form-group"> <!-- Biografia -->'+
                '<label for="message-text" class="col-form-label">Parafernalias:</label>'+
                '<textarea class="form-control" id="message-text" readonly> Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nihil, illum dolorum animi impedit quae distinctio consequatur consequuntur odio quidem sapiente porro explicabo voluptatibus neque aliquam debitis ad ut laboriosam minus.</textarea>'+
              '</div> <!-- Biografia -->'+

              '<div class="form-group"> <!-- Biografia -->'+
                '<label for="message-text" class="col-form-label">Aliados:</label>'+
                '<textarea class="form-control" id="message-text" readonly> Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nihil, illum dolorum animi impedit quae distinctio consequatur consequuntur odio quidem sapiente porro explicabo voluptatibus neque aliquam debitis ad ut laboriosam minus.</textarea>'+
              '</div> <!-- Biografia -->'+

              '<div class="form-group"> <!-- Biografia -->'+
                '<label for="message-text" class="col-form-label">Enemigos:</label>'+
                '<textarea class="form-control" id="message-text" readonly> Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nihil, illum dolorum animi impedit quae distinctio consequatur consequuntur odio quidem sapiente porro explicabo voluptatibus neque aliquam debitis ad ut laboriosam minus.</textarea>'+
              '</div> <!-- Biografia -->'+

              '<table class="table table-sm" id="estadisticas">'+
                '<thead class="thead-dark"> '+
                    '<tr>'+
                      '<th scope="col">Atributo</th> '+
                      '<th> <center>1</center></th> '+
                      '<th> <center>2</center></th>'+
                      '<th> <center>3</center></th>'+
                      '<th> <center>4</center></th>'+
                      '<th> <center>5</center></th>'+
                      '<th> <center>6</center></th>'+
                      '<th> <center>7</center></th>'+
                    '</tr>'+
                '</thead>   '+
                '<tbody> '+
                  '<tr id = "fuer">'+
                     '<th scope="row">Fuerza</th>'+
'                     '+
                  '</tr>                   '+
                  '<tr id = "intel">'+
                    '<th scope="row">Inteligen</th>'+
'                    '+
                  '</tr>'+
                  '<tr id = "agil">'+
                    '<th scope="row">Agilidad</th>'+
'                    '+
                    '<td></td>'+
                    '<td></td>'+
                  '</tr>'+
                  '<tr id = "resi">'+
                    '<th scope="row">Resist</th>'+

                  '</tr>'+

                  '<tr id = "proy_en">'+
                    '<th scope="row">Proyect Energy</th>'+
                  '</tr>'+

                  '<tr id = "hab_comb">'+
                    '<th scope="row">Hab combat</th>'+
                  '</tr>'+
                '</tbody>'+
              '</table>'+
              '<!--Datos -->'+

            '</form>'+
          '</div>'+
        '</div>'+
      '</div>'+
    '</div>'
  );
}
function busquedaNombre(){
  return $("#busqueda_nombre input").val();
}
function busquedaCategoria(){
  return $("#busqueda_categoria select").val();
}
function busquedaGrupo(){
  return $("#busqueda_afiliacion input").val();
}
function probarBusqueda(){
  if(busquedaNombre().length > 0 )
    console.log(busquedaNombre());
  
  if(busquedaCategoria().length > 0 )
    console.log(busquedaCategoria());

  if(busquedaGrupo().length > 0 )
    console.log(busquedaGrupo());
  
}
function enviarPeticionBusqueda(){
  
  $.ajax({
    url:"/buscarPersonaje/",
    type:"GET",
    data:{ 
       nombre:busquedaNombre(),
       afiliacion:busquedaGrupo(),
       categoria:busquedaCategoria()
    },
    success: function(respuesta){ 
      listaRespuestas = JSON.parse(respuesta);
      $("#cuerpo_tabla").html("");
      for (var index = 0; index < listaRespuestas.length; index++) {
        $("#cuerpo_tabla").append(
          "<tr onclick="+'"'+"$('#ficha_personaje').modal('show');"+'"'+">"+
              '<th scope="row">'+index+'</th>'+
              '<td>'+listaRespuestas[index].nombre+'</td>'+
              '<td>'+busquedaGrupo()+'</td> '+
              '<td>'+busquedaCategoria()+'</td>'+
          '</tr>'
        );        
      }    
    },
    error: function(respuesta){ alert("Error Busqueda"); }    
  });
}
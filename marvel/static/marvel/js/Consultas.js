
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
function listaPersonajes(){//getpersonajes
  $.ajax({
    url:"/getPersonajes/",
    type:"GET",
    data:{ 
      dato:'obtener'
    },
    success: function(respuesta){ 
       listado = [];
       listado = respuesta.split('_');
       
       for(var indice = 0; indice < listado.length; indice ++){
         $('#sel_Person').append(
           "<option>"+listado[indice]+"</option>"
         );
       }      
       
    },
    error: function(respuesta){ alert("Error Busqueda"); }    
  });
}
function listaAfiliacion(){//getAfiliaciones
  $.ajax({
    url:"/getAfiliacion/",
    type:"GET",
    data:{ 
      dato:'obtener'
    },
    success: function(respuesta){ 
       listado = [];
       listado = respuesta.split('_');
       
       for(var indice = 0; indice < listado.length; indice ++){
         $('#sel_Afil').append(
           "<option>"+listado[indice]+"</option>"
         );
       }      
       
    },
    error: function(respuesta){ alert("Error Busqueda"); }    
  });
}
function personalisarFicha(nombre,nombreReal,universo,biografia,identidad,profesion,lugar,ed_civil,parientes,afiliaciones,altura,altura2,peso,ojo,pelo,poderes,parafernalia,aliados,enemigos,fuer,inte,agil,resis,proyec,habi){
  $("#titulo_ficha").html("");
  $("#titulo_ficha").html("<label>"+nombre+"-"+nombreReal+"("+universo+")</label>");
  $("#biografia_personaje").html(biografia);
  $("#nombreOriginal_Ficha").html('<input class="form-control" value="'+nombre+'" id="nombre-text" readonly></input>');
  $("#nombreReal_Ficha").html('<input class="form-control" value="'+nombreReal+'" id="nombre-text" readonly></input>');
  if(identidad == 'C'){
    $("#identidad_Ficha").html('<input class="form-control" value="Publica" id="nombre-text" readonly></input>')
  }else{
    $("#identidad_Ficha").html('<input class="form-control" value="Oculta" id="nombre-text" readonly></input>')
  }
  $("#profesion_Ficha").html('<input class="form-control" value="'+profesion+'" id="nombre-text" readonly></input>')
  $("#lugar_nac").html(lugar);
  if(ed_civil == 'S')
    $("#edoCivil_Ficha").html('<input class="form-control" value="Soltero" id="nombre-text" readonly></input>');
  else
    $("#edoCivil_Ficha").html('<input class="form-control" value="Casado" id="nombre-text" readonly></input>');
    $("#parientes").html(parientes);
    $("#afiliacion_ficha").html(afiliaciones);
    $("#altura1").html('<input class="form-control" value='+altura+' id="nombre-text" readonly>');
    if(altura2 == null)
      $("#altura2").html('<input class="form-control" value="no aplica" id="nombre-text" readonly>');
    else
      $("#altura2").html('<input class="form-control" value='+altura2+' id="nombre-text" readonly>');
    $("#peso1").html('<input class="form-control" value='+peso+' id="nombre-text" readonly>');
    $("#peso2").html('<input class="form-control" value='+peso+' id="nombre-text" readonly>');
    $("#c_ojo").html('<input class="form-control" value='+ojo+' id="nombre-text" readonly>');
    $("#c_pelo").html('<input class="form-control" value='+pelo+' id="nombre-text" readonly>');
    $("#poderes").html(poderes);
    listaParafer = parafernalia.split("_");
    $("#parafernalia").html("");
    listaParafer.forEach(function(dato){
      $("#parafernalia").append(dato + "\n");
    });
    $("#aliados").html(aliados);
    $("#enemigos").html(enemigos);

    llenarHabilida(fuer,"fuer","Fuerza");
    llenarHabilida(inte,"intel","Inteligencia");
    llenarHabilida(agil,"agil","Agilidad");
    llenarHabilida(resis,"resi","Resistencia");
    llenarHabilida(proyec,"proy_en","Proyect Energy");
    llenarHabilida(habi,"hab_comb","Hab Combat");

}
function crearModalFichaPerson(){
  $("#modal_personaje").html(
    '<div class="modal fade" id="ficha_personaje" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">'+
      '<div class="modal-dialog" role="document">'+
        '<div class="modal-content">'+
          '<div class="modal-header">'+
            '<h5 class="modal-title" id="exampleModalLabel">Ficha de Personaje</h5>'+
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
                  '<textarea class="form-control" id="biografia_personaje" readonly> Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nihil, illum dolorum animi impedit quae distinctio consequatur consequuntur odio quidem sapiente porro explicabo voluptatibus neque aliquam debitis ad ut laboriosam minus.</textarea>'+
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
                '<textarea class="form-control" id="lugar_nac" readonly> Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nihil, illum dolorum animi impedit quae distinctio consequatur consequuntur odio quidem sapiente porro explicabo voluptatibus neque aliquam debitis ad ut laboriosam minus.</textarea>'+
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
                '<textarea class="form-control" id="parientes" readonly> Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nihil, illum dolorum animi impedit quae distinctio consequatur consequuntur odio quidem sapiente porro explicabo voluptatibus neque aliquam debitis ad ut laboriosam minus.</textarea>'+
              '</div> <!-- Parientes -->'+

              '<div class="form-group"> <!-- Biografia -->'+
                '<label for="message-text" class="col-form-label">Grupos de Afiliacion:</label>'+
                '<textarea class="form-control" id="afiliacion_ficha" readonly> Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nihil, illum dolorum animi impedit quae distinctio consequatur consequuntur odio quidem sapiente porro explicabo voluptatibus neque aliquam debitis ad ut laboriosam minus.</textarea>'+
              '</div> <!-- Biografia -->'+

              '<div class="row"> <!--Fisico-->'+
                '<div class="col-2">'+
                  '<label >Altura:</label>'+
                '</div>'+
                '<div class="col-2" id="altura1">'+
                  '<input class="form-control" value="0" id="nombre-text" readonly>'+
                '</div> '+
                '<div class="col-2" id="altura2">'+
                  '<input class="form-control" value="0" id="nombre-text" readonly>'+
                '</div> '+

                '<div class="col-2">'+
                  '<label >Peso:</label>'+
                '</div>'+
                '<div class="col-2" id="peso1">'+
                  '<input class="form-control" value="0" id="nombre-text" readonly>'+
                '</div> '+

                '<div class="col-2" id="peso2">'+
                  '<input class="form-control" value="0" id="nombre-text" readonly>'+
                '</div> '+
              '</div> <!--Fisico-->'+

              '<div class="row"> <!--Fisico-->'+
                '<div class="col-2">'+
                  '<label >Ojos:</label>'+
                '</div>'+
                '<div class="col-4" id="c_ojo">'+
                  '<input class="form-control" value="azul" id="nombre-text" readonly>'+
                '</div>                 '+

                '<div class="col-2">'+
                  '<label >Pelo:</label>'+
                '</div>'+
                '<div class="col-4" id="c_pelo">'+
                  '<input class="form-control" value="negro" id="nombre-text" readonly>'+
                '</div>                 '+

              '</div> <!--Fisico-->'+

              '<div class="form-group"> <!-- Biografia -->'+
                '<label for="message-text" class="col-form-label">Poderes conocidos:</label>'+
                '<textarea class="form-control" id="poderes" readonly> Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nihil, illum dolorum animi impedit quae distinctio consequatur consequuntur odio quidem sapiente porro explicabo voluptatibus neque aliquam debitis ad ut laboriosam minus.</textarea>'+
              '</div> <!-- Biografia -->'+

              '<div class="form-group"> <!-- Biografia -->'+
                '<label for="message-text" class="col-form-label">Parafernalias:</label>'+
                '<textarea class="form-control" id="parafernalia" readonly> Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nihil, illum dolorum animi impedit quae distinctio consequatur consequuntur odio quidem sapiente porro explicabo voluptatibus neque aliquam debitis ad ut laboriosam minus.</textarea>'+
              '</div> <!-- Biografia -->'+

              '<div class="form-group"> <!-- Biografia -->'+
                '<label for="message-text" class="col-form-label">Aliados:</label>'+
                '<textarea class="form-control" id="aliados" readonly> Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nihil, illum dolorum animi impedit quae distinctio consequatur consequuntur odio quidem sapiente porro explicabo voluptatibus neque aliquam debitis ad ut laboriosam minus.</textarea>'+
              '</div> <!-- Biografia -->'+

              '<div class="form-group"> <!-- Biografia -->'+
                '<label for="message-text" class="col-form-label">Enemigos:</label>'+
                '<textarea class="form-control" id="enemigos" readonly> Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nihil, illum dolorum animi impedit quae distinctio consequatur consequuntur odio quidem sapiente porro explicabo voluptatibus neque aliquam debitis ad ut laboriosam minus.</textarea>'+
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
  $("#modal_afiliacion").html(   
  '<div class="modal fade" id="ficha_afiliacion" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">'+
      '<div class="modal-dialog" role="document">'+
        '<div class="modal-content">'+
          '<div class="modal-header">'+
            '<h5 class="modal-title" id="exampleModalLabel">Ficha de Afiliacion</h5>'+
          '</div>'+
          '<div class="modal-body">'+
              '<div class="row"> '+
                '<div class="col" id="titulo_ficha_afiliacion">'+
                  '<label >Nombre de Afiliacion</label><!-- Nombre -->'+
                '</div>'+
              '</div> '+
            '<form>'+

              '<div class="form-group"> <!-- Base operaciones -->'+
                '<label for="message-text" class="col-form-label">Base de Operaciones:</label>'+
                '<textarea class="form-control" id="base_op" readonly> Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nihil, illum dolorum animi impedit quae distinctio consequatur consequuntur odio quidem sapiente porro explicabo voluptatibus neque aliquam debitis ad ut laboriosam minus.</textarea>'+
              '</div> <!-- Base operaciones -->'+

              '<div class="form-group"> <!-- Integrantes actuales -->'+
                '<label for="message-text" class="col-form-label">Integrantes Actuales:</label>'+
                '<textarea class="form-control" id="int_act" readonly> Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nihil, illum dolorum animi impedit quae distinctio consequatur consequuntur odio quidem sapiente porro explicabo voluptatibus neque aliquam debitis ad ut laboriosam minus.</textarea>'+
              '</div> <!-- Biografia -->'+

              '<div class="form-group"> <!-- Viejos Integrantes -->'+
                '<label for="message-text" class="col-form-label">Integrantes Anteriores:</label>'+
                '<textarea class="form-control" id="int_inac" readonly> Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nihil, illum dolorum animi impedit quae distinctio consequatur consequuntur odio quidem sapiente porro explicabo voluptatibus neque aliquam debitis ad ut laboriosam minus.</textarea>'+
              '</div>'+              
            '</form>'+
          '</div>'+
        '</div>'+
      '</div>'+
    '</div>  '
  );
  $('#modal_pelea').html(
    '<div class="modal modal-fade bd-example-modal-lg" id="modal_batallas" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabel" aria-hidden="true">'+
        '<div class="modal-dialog modal-lg">'+          
          '<div class="modal-content">'+
          '<div class="modal-header">'+
          '<h5 class="modal-title" id="exampleModalLabel">Batallas</h5>'+
          '</div>'+
            '<table class="table table-hover table-dark">'+
              '<thead>'+
                '<tr>'+
                  '<th scope="col">#</th>'+
                  '<th scope="col">Etapa</th>   '+
                  '<th scope="col">Personaje 1</th> '+
                  '<th scope="col">Personaje 2</th>  '+
                  '<th scope="col">Resultado</th> '+
                  '<th scope="col">Duracion</th>  '+
                  '<th scope="col">Fecha de Inicio</th>         '+
                '</tr>'+
              '</thead>'+
              '<tbody id="datosBatallas">'+
                 
              '</tbody>'+
            '</table>'+
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
          "<tr onclick="+'"'+" personalisarFicha('"+listaRespuestas[index].nombre+"','"
                                                  +listaRespuestas[index].nombre_real +" "+listaRespuestas[index].apellido_real+"','"
                                                  +listaRespuestas[index].universo+"','"
                                                  +listaRespuestas[index].biografia+"','"
                                                  +listaRespuestas[index].tipo_iden+"','"
                                                  +listaRespuestas[index].profesion+"','"
                                                  +listaRespuestas[index].lugar+"','"
                                                  +listaRespuestas[index].edo_civil+"','"
                                                  +listaRespuestas[index].parientes+"','"
                                                  +listaRespuestas[index].afiliaciones+"','"
                                                  +listaRespuestas[index].altura+"','"
                                                  +listaRespuestas[index].altura_arm+"','"
                                                  +listaRespuestas[index].peso+"','"
                                                  +listaRespuestas[index].color_ojo+"','"
                                                  +listaRespuestas[index].color_pelo+"','"
                                                  +listaRespuestas[index].poderes+"','"
                                                  +listaRespuestas[index].parafernalia+"','"
                                                  +listaRespuestas[index].aliados+"','"
                                                  +listaRespuestas[index].enemigos+"','"
                                                  +listaRespuestas[index].fuer+"','"
                                                  +listaRespuestas[index].inteligencia+"','"
                                                  +listaRespuestas[index].agilidad+"','"
                                                  +listaRespuestas[index].resistencia+"','"
                                                  +listaRespuestas[index].proyeccion+"','"
                                                  +listaRespuestas[index].habilidad+"'); $('#ficha_personaje').modal('show');"+'">'+
              '<th scope="row">'+index+'</th>'+
              '<td>'+listaRespuestas[index].nombre+'</td>'+
              '<td>'+listaRespuestas[index].afiliaciones+'</td> '+
              '<td>'+busquedaCategoria()+'</td>'+
          '</tr>'
        );        
      }    
    },
    error: function(respuesta){ alert("Error Busqueda"); }    
  });
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
//--------------------------------------------------------------------EVENTOS------------------------------------
function buscarEvento(){//perdir eventos
  alert("Enviando peticion a la funcion buscarEvento(request): la fecha: " + busquedaFecha());
  $.ajax({
    url:"/buscarEvento/",
    type:"GET",
    data:{ 
      fecha: busquedaFecha()
    },
    success: function(respuesta){ 
       superLista = JSON.parse(respuesta);  
       indiceRes = 0;     
       superLista.forEach(function(elemento){                   
      
         $("#cuerpo_tabla_eventos").html("");
         $("#cuerpo_tabla_eventos").append(
          "<tr onclick='"+
                          'var jsonDatos = '+elemento.Batallas+';'+
                          'cicloDeInfo(jsonDatos);'+
                          "$("+'"'+'#modal_batallas'+'"'+").modal("+'"'+'show'+'"'+");'>"+
              '<th scope="row">'+0+'</th>'+
              '<td>'+elemento.fech_in+'</td>'+
              '<td>'+elemento.fech_fin+'</td>'+   
              '<td>'+elemento.Duracion+' Dias</td>'+              
              '<td>'+elemento.Ganador+'</td>'+   
              '<td>'+elemento.Lugar+'</td>'+             
          '</tr>'
          );
       });

    },
    error: function(respuesta){ alert("Error Busqueda"); }    
  });
}
function busquedaFecha(){
  return $("#busqueda_fecha input").val();
}
//-------------------------------------------------------------------AFILIACION----------------------------------
function busquedaAFiliacionNombre(){
  return $("#sel_Afil").val();
}
function busquedaMiembro(){
  return $("#sel_Person").val();
}
function buscarAfiliacion(){  
  $.ajax({
    url:"/buscarAfiliacion/",
    type:"GET",
    data:{ 
      nombre:busquedaAFiliacionNombre(),
      miembro:busquedaMiembro()
    },
    success: function(respuesta){ 
      listaRespuestas = JSON.parse(respuesta);      
      $("#cuerpo_tabla_afiliacion").html("");
      for (var index = 0; index < listaRespuestas.length; index++) {
        $("#cuerpo_tabla_afiliacion").append(
          "<tr onclick="+'"'+"generarFichaAfil('"+listaRespuestas[index].nombre+"','"+listaRespuestas[index].lugar+"','"+listaRespuestas[index].miembros_actuales+"','"+listaRespuestas[index].antiguos_miembros+"');$('#ficha_afiliacion').modal('show');"+'">'+
              '<th scope="row">'+index+'</th>'+
              '<td>'+listaRespuestas[index].nombre+'</td>'+
              '<td>'+listaRespuestas[index].indice_pod+'</td>'+              
          '</tr>'
        );
      }
    },
    error: function(respuesta){ alert("Error Busqueda"); }    
  });
}
function generarFichaAfil(nombre,baseOp,intActiv,intInact){
  $("#titulo_ficha_afiliacion").html("<label >"+nombre+"</label>");
  $("#base_op").html(baseOp);
  $("#int_act").html(intActiv);
  $("#int_inac").html(intInact);
}
function cicloDeInfo(jsonDatos){
  $("#datosBatallas").html('');
  indice = 1;
  jsonDatos.forEach(function(element){
    llenarBatalla(indice,element.etapa,element.person1,element.person2,element.ganador,element.duracion,element.fecha);
    indice++;
  });
  
}

function llenarBatalla(num,etapa,per1,per2,ganador,dura,fech){
  v_ganador = "";
  if (ganador != "Empate"){
    v_ganador = "Ganador: " + ganador;
  }else{
    v_ganador = ganador;
  }
  $("#datosBatallas").append( 
  '<tr>'+
  '<td>'+num+'</td>'+
  '<td>'+etapa+'</td>'+
  '<td>'+per1+'</td>'+
  '<td>'+per2+'</td>'+
  '<td>'+ganador+'</td>'+
  '<td>'+dura+' Min </td>'+
  '<td>'+fech+'</td>'+
  '</tr>'
  );
}


//----------------------------GRUPO CON MAS GANADORES ---------------------------------------
function buscarGrupoConMasGanadores(){  
  $.ajax({
    url:"/buscarGrupoMasGanador/",
    type:"GET",
    data:{ 
      data:"buscar"
    },
    success: function(respuesta){ 
      //listado = JSON.parse(respuesta);
      console.log(JSON.parse(respuesta))
      $('#tablon_resultados_ganador_grupo').css('display','block');
      $("#cuerpo_tabla_ganador_grupo").html('');
      $("#cuerpo_tabla_ganador_grupo").append( 
          '<tr>'+
          '<td>'+JSON.parse(respuesta).ganador+'</td>'+
          '<td>'+JSON.parse(respuesta).evento+'</td>'+
          '<td>'+JSON.parse(respuesta).afiliacion+'</td>'+
          '<td>'+JSON.parse(respuesta).victorias+'</td>'+        
          '</tr>'
      );                 
    },
    error: function(respuesta){ alert("Error Busqueda"); }    
  });
}

function reiniciarBusquedas(){ 
  $('#tablon_resultados_ganador_grupo').css('display','none');
  $('#tablon_resultados_eventos').css('display','none');
  $('#tablon_resultados_afiliaciones').css('display','none');
  $('#tablon_resultados').css('display','none'); 
  $('#tablon_resultados_top').css('display','none');
 }

 function buscarTop3(){
  $.ajax({
    url:"/topGanadores/",
    type:"GET",
    data:{ 
      data:"buscar"
    },
    success: function(respuesta){ 
     lista = JSON.parse(respuesta);
     $('#tablon_resultados_top').css('display','block');
     indice = 1;
     $("#cuerpo_tabla_top").html('');
     lista.forEach(function(element){      
      $("#cuerpo_tabla_top").append( 
          '<tr>'+
          '<td>'+indice+'</td>'+
          '<td>'+element.personaje+'</td>'+
          '<td>'+element.afiliacion+'</td>'+
          '<td>'+element.victoriasEventos+'</td>'+
          '<td>'+element.victoriasPeleas+'</td>'+                 
          '</tr>'
      );  
      indice++;
     });               
    },
    error: function(respuesta){ alert("Error Busqueda"); }    
  });
 }
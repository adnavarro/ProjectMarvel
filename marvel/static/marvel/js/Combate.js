listaIdCombatientesActuales = [];
numeroGrupoActual = 0;
numEvento = 0;
cantidadDeRepeticiones = 0;
cantidadTope = 0;
combinacionesBetadas = [];
listaPersonajes = [];


function prepararContendientes(numGrupo,numEvent,token){ 
    numeroGrupoActual = numGrupo;
    numEvento = numEvent;

    $.ajax({
        url: "/getInscrit/",
        type: "GET",
        data:{ 
            numGrup:numGrupo,
            numEvent:numEvent              
        },
        success: function(respuesta){ 
            listaIdPersonajes = respuesta.split(",");            
            listaDeNombres(listaIdPersonajes,numGrupo,token);            
            listaIdCombatientesActuales = listaIdPersonajes; 
            cantidadTope = ( (factorial(listaIdCombatientesActuales.length)/(2*factorial(listaIdCombatientesActuales.length-2))) );
                   
        },
        error: function(respuesta){}    
    });
}
function listaDeNombres(listaIdPersonajes,numGrupo,token){
    $.ajax({
        url:"/personInGroup/",
        type:"GET",
        data:{ 
            "lista[]":JSON.stringify(listaIdPersonajes),                        
        },
        success: function(respuesta){ 
            listaTemporal = respuesta.split(",");             
            if(listaTemporal.length > listaIdPersonajes.length){
                listaTemporal.pop();                
            }           
            listaPersonajes = listaTemporal;

            mostrarLista(listaTemporal,numGrupo);            
        },
        error: function(respuesta){ alert("Error")}    
    });
}
function mostrarLista(listaPersonajes,numeroGrupo){
    $("#nombre_personaje").html(""); //titulo_lista_personajes  
    $("#titulo_lista_personajes").html("<h2>Grupo " + numeroGrupo+"</h2>");
    listaPersonajes.forEach(function(id){
        $("#nombre_personaje").append('<button type="button" class="list-group-item list-group-item-action">'+id+'</button>');
    });
    
}
function siguienteGrupo() {
    total = parseInt(sessionStorage.getItem("totalGrupos"));
    actual = parseInt(sessionStorage.getItem("actualGroup"));
    combinacionesBetadas = [];
    if(actual == (total-1) ){
        $("#siguiente_combate").attr('class', 'btn btn-success my-2 my-sm-0');
        $("#siguiente_combate").html("Siguiente Evento");
    }
    if(actual < total){
        actual++;
        sessionStorage.setItem("actualGroup",actual);
        prepararContendientes(""+actual,sessionStorage.getItem("eventoActual"),"");
    }else{
        alert("Reseteo, Evento2");       
    }
    $("#siguiente_combate").attr("disabled",true);
    $("#simular_combate").attr("disabled",false); 
}
function peleaValida(combatiente1,combatiente2){
    if(combinacionesBetadas.length > 0){
        for (var indice = 0; indice < combinacionesBetadas.length; indice++) {
            if(combinacionesBetadas[indice].includes(""+combatiente1) && combinacionesBetadas[indice].includes(""+combatiente2) ){
                return false;   
            }            
        }
        return true;
    }else{
        return true;
    }
}
function devolverLuchador(){    
    var min=1; 
    var max = listaIdCombatientesActuales.length;     
    var combatiente = Math.round(Math.random() * (+max - +min) + +min);
    return combatiente;
}

function emparejarCombates(nroFase){      
        $("#simular_combate").attr("disabled",true);  
        $("#siguiente_combate").attr("disabled",true);             
        if(combinacionesBetadas.length < cantidadTope){
                     
            var combatiente_1 = devolverLuchador();
            var combatiente_2 = combatiente_1;
            while(combatiente_2 === combatiente_1){
                combatiente_2 = devolverLuchador();
            }
            var permitirCombate = peleaValida(listaIdCombatientesActuales[combatiente_1-1],listaIdCombatientesActuales[combatiente_2-1]);
            if(permitirCombate){              
                combinacionesBetadas.push("["+listaIdCombatientesActuales[combatiente_1-1]+"-"+listaIdCombatientesActuales[combatiente_2-1]+"]");          
                combatir(listaIdCombatientesActuales[combatiente_1-1],listaIdCombatientesActuales[combatiente_2-1],listaIdCombatientesActuales.indexOf(listaIdCombatientesActuales[combatiente_1-1]),listaIdCombatientesActuales.indexOf(listaIdCombatientesActuales[combatiente_2-1]),nroFase);                                 
            }else{  
               //alert(combinacionesBetadas.length+" - " + cantidadTope);              
                setTimeout(function() {emparejarCombates(nroFase);}, 100);
            }     
        }else{              
            obtenerPrimerLugar(""+numEvento,""+numeroGrupoActual,nroFase);          
            $("#siguiente_combate").attr("disabled",false); 
        }
              
}
function combatir(primerPersonaje,segundoPersonaje,indice_1,indice_2,nroFase){  
    $.ajax({
        url:"/combate/",
        type:"GET",
        data:{ 
            primerPersonaje:""+primerPersonaje,
            segundoPersonaje:""+segundoPersonaje,
            numGrupo:""+numeroGrupoActual,
            numEvento:""+numEvento,
            numFase:nroFase
        },
        success: function(respuesta){ 
           if(respuesta === "Hubo un empate"){            
            mostrarResultados(listaPersonajes[indice_1],listaPersonajes[indice_2],respuesta,"1h");
            combatir(primerPersonaje,segundoPersonaje,indice_1,indice_2,nroFase);
           }else if( respuesta === "Gano el personaje 1"){           
           
            mostrarResultados(listaPersonajes[indice_1],listaPersonajes[indice_2],listaPersonajes[indice_1],"1h");
            emparejarCombates(nroFase);
           }else if( respuesta === "Gano el personaje 2"){           
            mostrarResultados(listaPersonajes[indice_1],listaPersonajes[indice_2],listaPersonajes[indice_2],"1h");
            emparejarCombates(nroFase);
           }else if(respuesta === "Gano un zombie"){
               alert("Error zombie");
           }
           
        },
        error: function(respuesta){ alert("Error combate")}    
    });
}
function mostrarResultados(nombrePersonaje1,nombrePersonaje2,resultado,tiempo){
    $("#cuerpo_tabla").append(
        '<tr>'+
        '<th scope="row"></th>'+
        '<td>'+nombrePersonaje1+'</td>'+
        '<td>'+nombrePersonaje2+'</td>'+
        '<td>'+resultado+'</td>'+
        '<td>'+tiempo+'</td>'+
        '</tr>'
    );    
}
function obtenerPrimerLugar(numeroEvento,numeroGrupo,numeroFase){
    try {
        $.ajax({
            url:"/ganador/",
            type:"GET",
            data:{ 
                numeroEven:numeroEvento,
                numeroGrup:numeroGrupo,
                numeroFas:numeroFase
            },success:function(respuesta){ 
                               
                if(respuesta === "empate"){
                    combinacionesBetadas = [];
                    emparejarCombates(numeroFase);
                }else{                    
                   if(sessionStorage.getItem("campeones_1")){
                        lista_ganador = JSON.parse(sessionStorage.getItem("campeones_1"));
                        lista_segundo = JSON.parse(sessionStorage.getItem("campeones_2"));
                        listaProcesada = respuesta.split(",");
                        ganador = listaProcesada[0];
                        segundo = listaProcesada[1];
                        ganador = ganador.split(":");
                        segundo = segundo.split(":");
                        ganador = ganador[1];
                        segundo = segundo[1];

                        lista_ganador.push(ganador);
                        lista_segundo.push(segundo);

                        sessionStorage.setItem("campeones_1",JSON.stringify(lista_ganador));
                        sessionStorage.setItem("campeones_2",JSON.stringify(lista_segundo));
                        mostrarGanador("cuerpo_tabla_primero_1",ganador,numeroGrupoActual,"x");
                        mostrarGanador("cuerpo_tabla_segundo_1",segundo,numeroGrupoActual,"x");
                   }else{    
                        lista_ganador = [];
                        lista_segundo = [];                    
                        listaProcesada = respuesta.split(",");
                        ganador = listaProcesada[0];
                        segundo = listaProcesada[1];
                        ganador = ganador.split(":");
                        segundo = segundo.split(":");
                        ganador = ganador[1];
                        segundo = segundo[1];

                        lista_ganador.push(ganador);
                        lista_segundo.push(segundo);
                        sessionStorage.setItem("campeones_1",JSON.stringify(lista_ganador));
                        sessionStorage.setItem("campeones_2",JSON.stringify(lista_segundo));
                        mostrarGanador("cuerpo_tabla_primero_1",ganador,numeroGrupoActual,"x");
                        mostrarGanador("cuerpo_tabla_segundo_1",segundo,numeroGrupoActual,"x");
                   } 
                }
            },error:function(repsuesta){
                alert("Error");
            }
        }); 
    } catch (error) {
        alert("Fallo");
    }
    
}
function mostrarGanador(idTabla,personaje,grupo,puntos){
    $("#"+idTabla).append(
        '<tr>'+
        '<th scope="row"></th>'+
        '<td>'+personaje+'</td>'+
        '<td>'+grupo+'</td>'+
        '<td>'+puntos+'</td>'+        
        '</tr>'
    ); 
}
function factorial(numero){
    if(numero === 1){
        return 1;
    }else
        return  numero * factorial(numero-1);
}
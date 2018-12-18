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
            alert(cantidadTope);         
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
                alert("Pop");
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
    if(actual < total){
        actual++;
        sessionStorage.setItem("actualGroup",actual);
        prepararContendientes(""+actual,sessionStorage.getItem("eventoActual"),"");
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

function emparejarCombates(){      
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
                combatir(listaIdCombatientesActuales[combatiente_1-1],listaIdCombatientesActuales[combatiente_2-1],listaIdCombatientesActuales.indexOf(listaIdCombatientesActuales[combatiente_1-1]),listaIdCombatientesActuales.indexOf(listaIdCombatientesActuales[combatiente_2-1]) );                                 
            }else{  
               //alert(combinacionesBetadas.length+" - " + cantidadTope);              
                setTimeout(emparejarCombates, 50);
            }     
        }else{
            alert("Fin de peleas");            
            $("#siguiente_combate").attr("disabled",false); 
        }
              
}
function combatir(primerPersonaje,segundoPersonaje,indice_1,indice_2){
   console.log(listaPersonajes);
   console.log("Numeros:" + indice_1 + " - " + indice_2 + " Combatientes actuales:" + listaPersonajes);
    $.ajax({
        url:"/combate/",
        type:"GET",
        data:{ 
            primerPersonaje:""+primerPersonaje,
            segundoPersonaje:""+segundoPersonaje,
            numGrupo:""+numeroGrupoActual,
            numEvento:""+numEvento
        },
        success: function(respuesta){ 
           if(respuesta === "Hubo un empate"){            
            mostrarResultados(listaPersonajes[indice_1],listaPersonajes[indice_2],respuesta,"1h");
            combatir(primerPersonaje,segundoPersonaje,indice_1,indice_2);
           }else if( respuesta === "Gano el personaje 1"){           
           
            mostrarResultados(listaPersonajes[indice_1],listaPersonajes[indice_2],listaPersonajes[indice_1],"1h");
            emparejarCombates();
           }else if( respuesta === "Gano el personaje 2"){           
            mostrarResultados(listaPersonajes[indice_1],listaPersonajes[indice_2],listaPersonajes[indice_2],"1h");
            emparejarCombates();
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
function factorial(numero){
    if(numero === 1){
        return 1;
    }else
        return  numero * factorial(numero-1);
}
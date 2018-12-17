listaIdCombatientesActuales = [];
numeroGrupoActual = 0;
numEvento = 0;
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
            listaPersonajes = respuesta.split(",");
            mostrarLista(listaPersonajes,numGrupo);            
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

    if(actual < total){
        actual++;
        sessionStorage.setItem("actualGroup",actual);
        prepararContendientes(""+actual,sessionStorage.getItem("eventoActual"),"");
    }
}
function emparejarCombates(){
    console.log(listaIdCombatientesActuales);
    var max = listaIdCombatientesActuales.length;
    var min=1;      
    var combatiente_1 = Math.round(Math.random() * (+max - +min) + +min); 
    var combatiente_2 = combatiente_1;
    while(combatiente_2 === combatiente_1){
        combatiente_2 = Math.round(Math.random() * (+max - +min) + +min);
    }
    combatir(listaIdCombatientesActuales[combatiente_1-1],listaIdCombatientesActuales[combatiente_2-1]);
}
function combatir(primerPersonaje,segundoPersonaje){
    alert(primerPersonaje+"Versus"+segundoPersonaje);
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
           alert("Peticion enviada")        
        },
        error: function(respuesta){ alert("Error combate")}    
    });
}
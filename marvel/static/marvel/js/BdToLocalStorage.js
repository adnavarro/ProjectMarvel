/*  |1° Los se deben crear los grupos en la pagina battle con el nombre de grupo_(numero de grupo)
    |Nota: empieza los grupos desde 1 hasta 4
    |2° Guarda de 3 en 3 los personajes de marvel en cada grupo correspondientes 
    |3° darle al boton empezar batalla para que se envien los datos, se enviara un JSON al Django que lo recibira la funcion search en views.py
    |Nota: la info recibida estara compactada por grupos, cada grupos tienen los id de los personajes correspondientes.
    |El return  que de search en views.py lo recivira el ajax en el succes(respuesta)
    
*/
function postEventRquests(token){       
    var lugar = $("#lugar_input").val();
    var duracion = $("#dias_select").val();
    if(lugar.length > 0 && duracion.length > 0 && duracion <= 3){
        $.ajax({
            url: "/insertEvento/",
            type: "POST",
            data:{ 
                lugar: lugar,
                duracion: duracion,
                csrfmiddlewaretoken:token
            },            
            success: function(json){            
                if(json === "fallo")
                    alert("No se pudo crear el evento");
                else if (json === "fallo_lugar"){
                    alert("El lugar no se encuentra en la base de datos");
                }
                else if (json === "fallo_duracion"){
                    alert("La duracion debe ser de maximo 3 dias");
                }else if (json === "fallo_duracion_min"){
                    alert("La duracion debe ser de minimo 1 dia");
                }
                else{
                    sessionStorage.setItem("eventoActual",""+json);
                    $('#exampleModal').modal("hide");
                }
                
            },error:function(data){
                alert("fallo el envio");                
            }
          });         
    }else{
        alert("los campos son invalidos");
    }          
}
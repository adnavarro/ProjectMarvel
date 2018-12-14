/*  |1° Los se deben crear los grupos en la pagina battle con el nombre de grupo_(numero de grupo)
    |Nota: empieza los grupos desde 1 hasta 4
    |2° Guarda de 3 en 3 los personajes de marvel en cada grupo correspondientes 
    |3° darle al boton empezar batalla para que se envien los datos, se enviara un JSON al Django que lo recibira la funcion search en views.py
    |Nota: la info recibida estara compactada por grupos, cada grupos tienen los id de los personajes correspondientes.
    |El return  que de search en views.py lo recivira el ajax en el succes(respuesta)
    
*/
function postResquesttt(token){
    $("#enviarData").submit(function(e){
        e.preventDefault();
    });
    grupo = [];
    numGrupo = 1;
    jsonDatoPreparado = [{}]
    while(true){
        if(!sessionStorage.getItem("miembros_grupo_"+numGrupo))
            break;
        
            grupo.push(JSON.parse(sessionStorage.getItem("miembros_grupo_"+numGrupo)))
         jsontemporal = {
             "fk_person":grupo[0],
             "n_grupo":numGrupo
         }         
         jsonDatoPreparado.push(jsontemporal);
         //console.log(sessionStorage.getItem("miembros_grupo_"+numGrupo) + "\n");
        if(numGrupo == 10)
            break;        
        numGrupo++;
    }     
    console.log(grupo)
    console.log(grupo);
    $("#enviarData").submit(function(e){
        e.preventDefault();

        $.ajax({
            url: $(this).attr('action'),
            type: "POST",
            data:{ 
                  datos:grupo,
                  csrfmiddlewaretoken: token
                },            
            success: function(json){
             alert("Enviado"); 
             alert(grupo);
                
            },error:function(data){
                alert("fallo:");
                //location.reload();
            }
          });
    })
       
}
$(function(){
    $.get('/cursos',function(data){
        console.log("Mensaje: "+ data[0])        
    });
});

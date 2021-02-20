$(document).ready(function(){
    console.log("si entra")
    function ajax_login(){
        $.ajax({
            url:'/ajax-login',
            data: $('form').serialize(),
            type : 'POST',
            sucess: function(response){
                console.log(response);
            },
            error: function(error){
                console.log(error);
            }
        });
    }
    $("#obtener").submit(function(event){
        event.preventDefault();
        ajax_login();
    });
});
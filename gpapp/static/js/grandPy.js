
$(document).ready(function(){
    function answer_gp(response){
        console.log('la reponse'+ response);
        $('.home').hide();
        $('#gp_reply').show();
        $('.answer').show();
        $('#gp_reflection').hide();
    };
    $('#submit2').submit(function(e){

    /*
     *send a question to GrandPy
    */
        $('.home').hide();
        $('#gp_reflection').show();
        $.ajax({
            url: '/index/3',
            type: 'GET',
            dataType: 'html',
            success: answer_gp
        });
        e.preventDefault();
    });

});


$(document).ready(function(){
    function display(response_json){
        var instruction = [
                $('#ask').hide(),
                $('#word_of_welcome').hide(),
                $('#gp_reflection').hide(),
                $('#answer').show(),
                $('#other').show()
        ]
        var wiki_answer = response_json['answer']['history'];
        instruction.push(
            $('#address').text("l'adresse "+wiki_answer[0]+" se situe : "
            + JSON.stringify(response_json['answer']['address']['result']['formatted_address'])));

        instruction.push($('#map')[0].src = response_json['display_map']);

        if (wiki_answer[2][0]){
            var texte = $('#history').text(JSON.stringify(wiki_answer[2][0]));
        }
        else{
            var texte = $('#history').text('Aie aie aie, le \'WIKI\' est vide... !');
        }

        instruction.push(texte);

        return instruction
    };

    function answer_gp(response){
        var response_json = JSON.parse(response);
        var lt_mes =[
                    "#gp_reply4","#gp_reply5",
                    "#gp_reply6","#gp_reply7"
        ];

        console.log(response_json);
        if (response_json["quotas_api"]["nb_response"] == 1){

            $("#gp_reply3").show();
            $.each(display(response_json), function(value){
                $(value)
                }
            );
        }
        else if (response_json["quotas_api"]["nb_response"] == 5){

            $("#overstrain").show();
            $.each(display(response_json), function(value){
                $(value)
                }
            );
        }
        else if ((response_json["quotas_api"]["over_quotas"] == "True") ||
                (response_json["quotas_api"]["nb_response"] == 10)){

            $("#quotas").show();
            $("#window_sill").hide();
            $("#other").hide();
            $("#gp_reflection").hide();
            $("#ask").hide();
        }
        else if (response_json["quotas_api"]["comprehension"] == "False"){

            $("#comprehension").show();
            $("#question").val(" ");
            $.each(display(response_json), function(value){
                $(value)
                }
            );
        }
        else{
                $(lt_mes[Math.floor(Math.random()*lt_mes.length)]).show();
                $.each(display(response_json), function(value){
                    $(value)
                    }
                );
        }
    };

    $("#submit2").submit(function(e){

    /*
     *send a question to GrandPy
    */
        $("#word_of_welcome").hide();
        $("#comprehension").hide();
        $("#gp_reflection").show();
        $.ajax({
            url: "/index/2/" + $("#question").val().toString(),
            type: "GET",
            dataType: "html",
            success: answer_gp
        });
        e.preventDefault();
    });

});

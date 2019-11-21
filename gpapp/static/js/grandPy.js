
$(document).ready(function(){
    function display(response_json){

        var instruction = [
                $('#ask').hide(),
                $('#word_of_welcome').hide(),
                $('#gp_reflection').hide(),
                $('#comprehension').hide(),
                $('#gp_reply').show(),
                $('#answer').show(),
                $('#other').show()
        ]
        instruction.push(
            $('#address').text("l'adresse se situe : "
            + JSON.stringify(response_json['answer']['address']['result']['formatted_address'])));

        instruction.push($('#map')[0].src = response_json['display_map']);

        var wiki_answer = response_json['answer']['history'];
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
        if (response_json["quotas_api"]["nb_response"] == 5){

            $("#ask").hide();
            $("#word_of_welcome").hide();
            $("#gp_reflection").hide();
            $("#comprehension").hide();
            $("#overstrain").show();
            $("#answer").show();
            $("#other").show();
            $.each(display(response_json), function(index, value){
                $(value);
            });

        }
        else if ((response_json["quotas_api"]["over_quotas"] == "True") ||
                (response_json["quotas_api"]["nb_response"] >= 10)){
            $("#gp_reflection").hide();
            $("#ask").hide();
            $("#other").hide();
            $("#window_sill").hide();
            $("#quotas").show();
        }
        else if (response_json["quotas_api"]["comprehension"] == "False"){
            $("#gp_reflection").hide();
            $("#ask").hide();
            $("#other").hide();
            $("#ask").show();
            $("#comprehension").show();

        }
        else{
            $.each(display(response_json), function(index, value){
                $(value);
            });
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


$(document).ready(function(){
    function answer_gp(response){
        var response_json = JSON.parse(response);
        console.log(response_json);
        if (response_json["quotas_api"]["nb_response"] == 5){

            $("#ask").hide();
            $("#word_of_welcome").hide();
            $("#gp_reflection").hide();
            $("#comprehension").hide();
            $("#overstrain").show();
            $("#answer").show();
            $("#other").show();

        }
        else if ((response_json["quotas_api"]["over_quotas"] == "True") || (response_json["quotas_api"]["nb_response"] >= 10)){
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
            $("#question").text.value(" ");
            $("#ask").show();
            $("#comprehension").show();
        }
        else{
            $("#ask").hide();
            $("#word_of_welcome").hide();
            $("#gp_reflection").hide();
            $("#comprehension").hide();
            $("#gp_reply").show();
            $("#answer").show();
            $("#other").show();

            $("#address").text("l'adresse se situe : "
                                +JSON.stringify(response_json["answer"]["address"]["result"]["formatted_address"]));
            $("#map")[0].src = response_json["display_map"];

            wiki_answer = response_json["answer"]["history"];

            if (wiki_answer[2][0]){
                $("#history").text(JSON.stringify(wiki_answer[2][0]));
            }
            else{
                $("#history").text("Aie aie aie, le 'WIKI' est vide... !");
            }
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

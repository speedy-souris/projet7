
$(document).ready(function(){
    /** Display of the answers by default
      * with and without the constraints
      * (number of questions, misunderstanding, lack of respect ...)
    */

    //------------------------
    // default answer display (without constraints)
    function display(response_json){
        var instruction = [
                $("#ask").hide(),
                $("#word_of_welcome").hide(),
                $("#gp_reflection").hide(),
                $("#gp_reply2").hide(),
                $("#question").val(""),
                $("#answer").show(),
                $("#other").show()
        ]
        /** redisplay question and
          * display map / address / history (wiki)
       */
        var wiki_answer = response_json["answer"]["history"];
        instruction.push(
            $("#address").text("l'adresse "+wiki_answer[0]+" se situe : "
            + JSON.stringify(response_json["answer"]["address"]["result"]["formatted_address"])));

        instruction.push($("#map")[0].src = response_json["display_map"]);

        if (wiki_answer[2][0]){
            var texte = $("#history").text(JSON.stringify(wiki_answer[2][0]));
        }
        else{
            var texte = $("#history").text("Aie aie aie, le \'WIKI\' est vide... !");
        }

        // Add wiki
        instruction.push(texte);

        return instruction
    };

    //------------------------
    // general display of responses with constraints
    function answer_gp(response){
        var response_json = JSON.parse(response);
        var lt_mes =[
                    "#gp_reply4","#gp_reply5",
                    "#gp_reply6","#gp_reply7"
        ];
        $("#question").val("");

        // answer display with politeness of the user
        if ((response_json["politeness"]["civility"] == true) &&
            (!response_json["quotas_api"]["over_quotas"])){
                // welcome message
                if (response_json["nb_response"] <= 1){

                    $("#gp_reflection").hide();
                    $("#word_of_welcome").show();
                    $("#ask").show();
                    console.log("j\'arrive ici");
                }

                // overwork message
                else if (response_json["nb_response"] == 5){

                    $("#overstrain").show();
                    $.each(display(response_json), function(value){
                        $(value);
                    }
                    );
                }
                // grandpy burnout message
                else if (response_json["nb_response"] == 10){

                    $("#quotas").show();
                    $("#window_sill").hide();
                    $("#other").hide();
                    $("#gp_reflection").hide();
                    $("#ask").hide();
                }
                // message of misunderstanding
                else if (response_json["quotas_api"]["comprehension"] == false){

                    $("#gp_reflection").hide();
                    $("#other").hide();
                    $("#ask").show();
                    $("#comprehension").show();

                }
                // message of disgrace for disrespect
                else if (response_json["politeness"]["decency"] == false){

                    $("#gp_reply1").hide();
                    $("#gp_reflection").hide();
                    $("#gp_reply2").show();
                    $("#ask").show();
                }
                // display answer requested
                else{
                        $(lt_mes[Math.floor(Math.random()*lt_mes.length)]).show();
                        $.each(display(response_json), function(value){
                            $(value);
                        }
                        );
                }
            }
        // quota overrun for API requests
        else{
                if (response_json["quotas_api"]["over_quotas"] == true){

                    $("#gp_reflection").hide();
                    $("#gp_reply1").hide();
                    $("#ask").hide();
                    $("#gp_tag").hide();
                    $("#quotas").show();
                }
                // // message of disgrace for disrespect
                else if (response_json["politeness"]["decency"] == false){

                    $("#gp_reply1").hide();
                    $("#gp_reflection").hide();
                    $("#gp_reply2").show();

                }
                else{

                    $("#gp_reply2").hide();
                    $("#gp_reflection").hide();
                    $("#gp_reply1").show();
                    $("#ask").show();
                    $("#question").val("");
                }


        }
    };

    //------------------------
    // send question
    $("#submit2").submit(function(e){

    /**
      * display and reflection time to the question
    */
        $("#gp_reply1").hide();
        $("#gp_reply2").hide();
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

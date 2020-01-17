$(document).ready(function(){
    /*
      * Display of the answers by default
      * with and without the constraints
      * (number of questions, misunderstanding, lack of respect ...)
    */

    /*
      *=================================
      * display with API quotas reached
      *=================================
    */
    function display_quotas(){

        var instruction = [
            $("#quotas").show(),
            $("#window_sill").hide(),
            $("#other").hide(),
            $("#gp_reflection").hide(),
            $("#ask").hide()
        ];
        return instruction
    };

    /*
      *=========================================
      * display answer on question not included
      *=========================================
    */
    function display_incomprehension(){

        var instruction = [
            $("#gp_reflection").hide(),
            $("#other").hide(),
            $("#comprehension").show(),
            $("#ask").show(),
            $("#question").val("")
        ];
        return instruction
    };

    /*
      *===================================
      * display answer without politeness
      *===================================
    */
    function display_politeness(){

        var instruction = [
            $("#gp_reply1").hide(),
            $("#gp_reflection").hide(),
            $("#gp_reply2").show(),
            $("#ask").show(),
            $("#question").val("")
        ];
        return instruction
    };

    /*
      *========================
      * default answer display
      * (without constraints)
      *========================
    */
    function display_default(response_json){

        var instruction = [
                $("#ask").hide(),
                $("#word_of_welcome").hide(),
                $("#gp_reflection").hide(),
                $("#gp_reply2").hide(),
                $("#question").val(""),
                $("#answer").show(),
                $("#other").show()
        ];
        /*
          * redisplay question and
          * display map / address / history (wiki)
       */
        var wiki_answer = response_json["map_status"]["answer"]["history"];
        instruction.push(
            $("#address").text("l'adresse "+wiki_answer[0]+" se situe : "
            + JSON.stringify(
                response_json["map_status"]["answer"]["address"]
                    ["result"]["formatted_address"]
                )
            )
        );

        instruction.push($("#map")[0].src = response_json["map_status"]["display_map"]);
        console.log(wiki_answer);
        if (wiki_answer[3][1]){
            var texte = $("#history").text(JSON.stringify(wiki_answer[3][1]));
        }else{
            var texte = $("#history").text("Aie aie aie, le \'WIKI\' est vide... !");
        };
        // Add wiki
        instruction.push(texte);

        return instruction
    };

    /*
      *===============================================
      * general display of responses with constraints
      *===============================================
    */
    function answer(response){
        var response_json = JSON.parse(response);
        var lt_mes =[
                    "#gp_reply4","#gp_reply5",
                    "#gp_reply6","#gp_reply7"
        ];
        $("#question").val("");
        console.log(response_json);

        // answer display with politeness of the user
        if ((response_json["parameter_status"]["civility"]) &&
            (!response_json["parameter_status"]["quotas_api"])){
                // welcome message
                if (response_json["parameter_status"]["nb_request"] <= 1){

                    $("#gp_reflection").hide();
                    $("#word_of_welcome").show();
                    $("#ask").show();
                // overwork message
                }else if (response_json["parameter_status"]["nb_request"] == 5){

                    $("#overstrain").show();
                    $.each(display_default(response_json), function(value){
                        $(value);
                    });
                // grandpy burnout message
                }else if (response_json["parameter_status"]["nb_request"] >= 10){

                    $.each(display_quotas(), function(value){
                        $(value);
                    });
                // message of misunderstanding
                }else if (!response_json["parameter_status"]["comprehension"]){

                    $.each(display_incomprehension(), function(value){
                        $(value);
                    });
                // message of disgrace for disrespect
                }else if (!response_json["parameter_status"]["decency"]){

                    $.each(display_politeness(), function(value){
                        $(value);
                    });
                // display answer requested
                }else{
                        $(lt_mes[Math.floor(Math.random()*lt_mes.length)]).show();
                        $.each(display_default(response_json), function(value){
                            $(value);
                        });
                };
        // quota overrun for API requests
        }else{
                if (!response_json["parameter_status"]["decency"]){

                    $.each(display_politeness(), function(value){
                        $(value);
                    });

                }else if (!response_json["parameter_status"]["comprehension"]){

                    $.each(display_incomprehension(), function(value){
                        $(value);
                    });

                }else if (response_json["parameter_status"]["quotas_api"]){

                    $.each(display_quotas(), function(value){
                        $(value);
                    });

                }else{

                    $("#gp_reply2").hide();
                    $("#gp_reflection").hide();
                    $("#gp_reply1").show();
                    $("#ask").show();
                    $("#question").val("");
                };
        };
    };

    /*
      *===============
      * send question
      *===============
    */
    $("#form_question").submit(function(e){

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
            success: answer
        });
        e.preventDefault();
    });

});

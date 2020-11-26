$(document).ready(function(){
    /*
      * Display of the answers by default
      * with and without the constraints
      * (number of questions, misunderstanding, lack of respect ...)
    */

    /*
      *========================
      * default answer display
      * (without constraints)
      *========================
    */
    const display_default = (response_json) => {

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

        if (wiki_answer[0][2]){
            var texte = $("#history").text(JSON.stringify(wiki_answer[0][2]));
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
    const answer = (response) => {
        var response_json = JSON.parse(response);
        var lt_mes =[
                    "#gp_reply4","#gp_reply5",
                    "#gp_reply6","#gp_reply7"
        ];
        console.log(response_json)
        
        
        
    }
    

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

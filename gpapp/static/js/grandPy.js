$(document).ready(function(){

    var $ask = $('#ask'),
        $word_of_welcome = $('#word_of_welcome'),
        $gp_reflection = $('#gp_reflection'),
        $gp_reply1 = $('#gp_reply1'),
        $gp_reply2 = $('#gp_reply2'),
        $gp_reply3 = $('#gp_reply3'),
        $gp_reply4 = $('#gp_reply4'),
        $gp_reply5 = $('#gp_reply5'),
        $gp_reply6 = $('#gp_reply6'),
        $gp_reply7 = $('#gp_reply7'),
        $question = $('#question'),
        $quotas = $('#quotas'),
        soverstrain = $('#overstarin'),
        $answer = $('#answer'),
        $other = $('#other'),
        $comprehension = $('#comprehension'),
        $address = $("#address"),
        $map = $('#map'),
        $history = $('#history'),
        $from_question = $('#from_question');

    const home_display = () => {
        [
            $ask.hide(),
            $word_of_welcome.hide(),
            $g_reflection.hide(),
            $reply2.hide(),
            $question.val(''),
            $answer.show(),
            $other.show()
        ];        
    };

    const request_display = () => {
        $gp_reply1.hide(),
        $gp_reply2.hide(),
        $word_of_welcome.hide(),
        $comprehension.hide(),
        $gp_reflection.show()
    };

    const politeness_display = () => {
        [
            $gp_reply1.hide(),
            $gp_reflection.hide(),
            $gp_reply2.show(),
            $ask.show(),
            $question.val("")
        ];
    };

    const incomprehension_display = () => {
        [
            $gp_reflection.hide(),
            $other.hide(),
            $comprehension.show(),
            $ask.show(),
            $question.val("")
        ];    
    };
    
    // random message from grandpyRobot
    const random_message = () => {
        var lt_mes =[
                    gp_reply4,gp_reply5,
                    gp_reply6,gp_reply7
        ];
        $(lt_mes[Math.floor(Math.random()*lt_mes.length)]).show();
    };

    /*
      * default answer display
      * (without constraints)
    */
    const display_default = (response_json) => {

        var instruction = home_display();
        /*
          * redisplay question and
          * display map / address / history (wiki)
       */
        var wiki_answer = response_json["map_status"]["answer"]["history"];
        instruction.push(
            $address.text("l'adresse "+wiki_answer[0]+" se situe : "
            + JSON.stringify(
                response_json["map_status"]["answer"]["address"]
                    ["result"]["formatted_address"]
            ))
        );

        instruction.push($map[0].src = response_json["map_status"]["display_map"]);

        if (wiki_answer[0][2]){
            var texte = $history.text(JSON.stringify(wiki_answer[0][2]));
        }else{
            var texte = $history.text("Aie aie aie, le \'WIKI\' est vide... !");
        };
        // Add wiki
        instruction.push(texte);

        return instruction
    };

    // general display of responses with constraints
    var answer = (response) => {
        var response_json = JSON.parse(response);
        var message = response_json["grandpy_message"];
        
    };

    // send question
    $form_question.submit(function(e){

        // display and reflection time to the question
        request_display();
        $.ajax({
            url: "/index/2/" + $("#question").val().toString(),
            type: "GET",
            dataType: "html",
            success: answer
        });
        e.preventDefault();
    });

});

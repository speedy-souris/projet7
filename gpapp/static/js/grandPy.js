$(document).ready(function(){

    const command_value = function(value) => {
        var command = '';
        switch (value) {
            case 'ask':
                command = $('#ask')
                break;
            case 'home':
                command  = $('#word_of_welcome')
                break;
            case 'relection':
                command = $('#gp_reflection')
                break;
            case 'mannerless':
                command = $('#gp_reply1')
                break;
            case 'rude':
                command = $('#gp_reply2')
                break;
            case 'politeness':
                command = $('#gp_reply3')
                break;
            case 'correct1':
                command = $('#gp_reply4')
                break;
            case 'correct2':
                command = $('#gp_reply5')
                break;
            case 'correct3':
                command = $('#gp_reply6')
                break;
            case 'correct4':
                command = $('#gp_reply7')
                break;
            case 'question':
                command = $('#question')
                break;
            case 'quotas':
                command = $('#quotas')
                break;
            case 'overstarin':
                command = $('#overstarin')
                break;
            case 'answer':
                command = $('#answer')
                break;
            case 'other':
                command = $('#other')
                break;
            case 'comprehension':
                command = $('#comprehension')
                break;
            case 'address':
                command = $('#address')
                break;
            case 'map':
                command = $('#map')
                break;
            case 'history':
                command = $('history')
                break;
            case 'form_question':
                command = $('#form_question')
                break;
            case 'ajax':
                command = $.ajax({
                    url: "/index/2/" + $('#question').val().toString(),
                    type: "GET",
                    dataType: "html",
                    success: answer
                });
        };
        return command
    };

    const home_display = function() => {
        [
            command_value('ask').hide(),
            command_value('word_of_welcome').hide(),
            command_value('gp_reflection').hide(),
            command_value('gp_reply2').hide(),
            command_value('question').val(''),
            command_value('answer').show(),
            command_value('other').show()
        ];        
    };

    const request_display = function() => {
        command_value('gp_reply1').hide();
        command_value('gp_reply2').hide();
        command_value('word_of_welcome').hide();
        command_value('comprehension').hide();
        command_value('gp_reflection').show();
    };

    const politeness_display = function() => {
        [
            command_value('gp_reply1').hide(),
            command_value('gp_reflection').hide(),
            command_value('gp_reply2').show(),
            command_value('ask').show(),
            command_value('question').val('')
        ];
    };

    const incomprehension_display = function() => {
        [
            command_value('gp_reflection').hide(),
            command_value('other').hide(),
            command_value('comprehension').show(),
            command_value('ask').show(),
            command_value('question').val('')
        ];    
    };
    
    // random message from grandpyRobot
    const random_message = function() => {
        var lt_mes =[
                    command_value('gp_reply4'),command_value('gp_reply5'),
                    command_value('gp_reply6'),command_value('gp_reply7')
        ];
        command_value('gp_reply4').hide()
        command_value('gp_reply5').hide()
        command_value('gp_reply6').hide()
        command_value('gp_reply7').hide()
        command_value('other').hide()
        command_value('gp_reflection').hide()
        command_value('question').val('')
        
        $(lt_mes[Math.floor(Math.random()*lt_mes.length)]).show();
    };

    /*
      * default answer display
      * (without constraints)
    */
    const display_default = function(response_json) => {

        var instruction = home_display();
        /*
          * redisplay question and
          * display map / address / history (wiki)
       */
        var wiki_answer = response_json["map_status"]["answer"]["history"];
        instruction.push(
            command_value('address').text("l'adresse "+wiki_answer[0]+" se situe : "
            + JSON.stringify(
                response_json["map_status"]["answer"]["address"]
                    ["result"]["formatted_address"]
            ))
        );

        instruction.push(command_value('map')[0].src = response_json["map_status"]["display_map"]);

        if (wiki_answer[0][2]){
            var texte = command_value('history').text(JSON.stringify(wiki_answer[0][2]));
        }else{
            var texte = command_value('history').text("Aie aie aie, le \'WIKI\' est vide... !");
        };
        // Add wiki
        instruction.push(texte);

        return instruction
    };

    // general display of responses with constraints
    const answer = function(response) => {
        var response_json = JSON.parse(response);
        console.log(response_json)
        random_message()
       
        
    };

    // send question
    command_value('form_question').submit(function(e){
        // display and reflection time to the question
        request_display();
        command_value('ajax');
        e.preventDefault();
    });

});

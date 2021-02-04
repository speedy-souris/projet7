$(document).ready(function(){

    const command_value = function(value) {
        var command = '';
        switch (value) {
            case 'ask':
                command = $('#ask');
                break;
            case 'home':
                command = $('#word_of_welcome');
                break;
            case 'reflection':
                command = $('#gp_reflection');
                break;
            case 'mannerless':
                command = $('#gp_reply1');
                break;
            case 'rude':
                command = $('#gp_reply2');
                break;
            case 'correct':
                command = $('#gp_reply3');
                break;
            case 'correct1':
                command = $('#gp_reply4');
                break;
            case 'correct2':
                command = $('#gp_reply5');
                break;
            case 'correct3':
                command = $('#gp_reply6');
                break;
            case 'correct4':
                command = $('#gp_reply7');
                break;
            case 'question':
                command = $('#question');
                break;
            case 'quotas':
                command = $('#quotas');
                break;
            case 'overstrain':
                command = $('#overstrain');
                break;
            case 'answer':
                command = $('#answer');
                break;
            case 'other':
                command = $('#other');
                break;
            case 'comprehension':
                command = $('#comprehension');
                break;
            case 'address':
                command = $('#address');
                break;
            case 'map':
                command = $('#map');
                break;
            case 'history':
                command = $('#history');
                break;
            case 'form_question':
                command = $('#form_question');
                break;
            case 'ajax':
                command = $.ajax({
                    url: "/index/2/" + $('#question').val().toString(),
                    type: "GET",
                    dataType: "html",
                    success: answer
                });
                break;
            default:
                console.log('commande non reconnue');
        };
        return command;
    };

    const home_display = function() {
        command_value('ask').hide();
        command_value('home').hide();
        command_value('reflection').hide();
        command_value('rude').hide();
        command_value('question').val('');
        command_value('answer').show();
        command_value('other').show();
    };

    const request_display = function() {
        command_value('mannerless').hide();
        command_value('rude').hide();
        command_value('home').hide();
        command_value('comprehension').hide();
        command_value('reflection').show();
    };

    const rudeness_display = function() {
        command_value('mannerless').hide();
        command_value('reflection').hide();
        command_value('rude').show();
        command_value('ask').show();
        command_value('question').val('');
    };

    const mannerless_display = function() {
        command_value('rude').hide();
        command_value('reflection').hide();
        command_value('mannerless').show();
        command_value('ask').show();
        command_value('question').val('');
    };

    const incomprehension_display = function() {
        command_value('reflection').hide();
        command_value('other').hide();
        command_value('comprehension').show();
        command_value('ask').show();
        command_value('question').val('');
    };

    // random message from grandpyRobot
    const random_message = function() {
        var lt_mes =[
                    command_value('correct1'),command_value('correct2'),
                    command_value('correct3'),command_value('correct4'),
                    command_value('correct')
        ];
        command_value('correct').hide();
        command_value('correct1').hide();
        command_value('correct2').hide();
        command_value('correct3').hide();
        command_value('correct4').hide();
        command_value('other').hide();
        command_value('reflection').hide();
        command_value('question').val('');

        $(lt_mes[Math.floor(Math.random()*lt_mes.length)]).show();
    };

    const ask_display = function() {
        command_value('reflection').hide();
        command_value('other').hide();
        command_value('home').show();
        command_value('question').val('');
    };

    const fatigue_display = function() {
        command_value('correct').hide();
        command_value('correct1').hide();
        command_value('correct2').hide();
        command_value('correct3').hide();
        command_value('correct4').hide();
        command_value('reflection').hide();
        command_value('other').hide();
        command_value('overstrain').show();
        command_value('question').val('');
    };

    const quotas_display = function() {
        command_value('rude').hide();
        command_value('mannerless').hide();
        command_value('comprehension').hide();
        command_value('reflection').hide();
        command_value('other').hide();
        command_value('ask').hide();
        command_value('quotas').show();
    };

    const display_default = function(response_json) {
    /*
      * default answer display
      * (without constraints)
    */
        home_display();
        /*
          * redisplay question and
          * display map / address / history (wiki)
       */
       if (response_json["map_status"]["answer"]){
            var wiki_answer = response_json["map_status"]["answer"]["history"];
            command_value('address').text("l'adresse "+wiki_answer[0]+" se situe : "
                + JSON.stringify(
                response_json["map_status"]["answer"]["address"]
                ["result"]["formatted_address"]
                )
            );
    
            command_value('map')[0].src = response_json["map_status"]["display_map"];
    
            if (wiki_answer[0][2]){
                var texte = command_value('history').text(JSON.stringify(wiki_answer[0][2]));
            }else{
                var texte = command_value('history').text("Aie aie aie, le \'WIKI\' est vide... !");
            };
            // Add wiki
           
        } else {
            var texte = command_value('map').text("aucun adresse n'a pas été trouvé");
        };
    };

    // general display of responses with constraints
    const answer = function(response) {
        var response_json = JSON.parse(response);
        console.log(response_json);
        if (response_json['grandpy_code'] === 'response'){
            random_message();
            display_default(response_json);
        }else if (response_json['grandpy_code'] === 'mannerless'){
            mannerless_display();
        }else if (response_json['grandpy_code'] === 'disrespectful'){
            rudeness_display();
        }else if (response_json['grandpy_code'] === 'incomprehension'){
            incomprehension_display();
        }else if (response_json['grandpy_code'] === 'tired'){
            fatigue_display();
            display_default(response_json);
        }else if (response_json['grandpy_code'] === 'exhausted'){
            quotas_display();
        }else {
            ask_display();
        };
    };

    // send question
    command_value('form_question').submit(function(e){
        // display and reflection time to the question
        request_display();
        command_value('ajax');
        e.preventDefault();
    });

});

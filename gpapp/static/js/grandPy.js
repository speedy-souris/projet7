
$(document).ready(function(){
    function answer_gp(response){
        var response_json = JSON.parse(response);
        $("#ask").hide();
        $("#word_of_welcome").hide();
        $("#gp_reply").show();
        $("#answer").show();
        $("#gp_reflection").hide();
        console.log(response);
        $("#address").text("l'adresse se situe : "
                            +JSON.stringify(response_json["address"]["result"]["formatted_address"]));

        $("#map").src = response["ref_map"];

        wiki_answer = response_json["history"];

        if (wiki_answer[2][0]){
            $("#history").text(JSON.stringify(wiki_answer[2][0]))
        }
        else{
            $("#history").text("Aie aie aie, le 'WIKI' est vide... !")
        };

    };

    $("#submit2").submit(function(e){

    /*
     *send a question to GrandPy
    */
        $("#word_of_welcome").hide();
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

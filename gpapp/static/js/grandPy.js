
$(document).ready(function(){
    function answer_gp(response){
        var response_json = JSON.parse(response);
        var localization = response_json["result"]["geometry"]["location"];
        var address = JSON.stringify(response_json["result"]["formatted_address"]);
        $("#ask").hide();
        $("#word_of_welcome").hide();
        $("#gp_reply").show();
        $("#answer").show();
        $("#gp_reflection").hide();

        $("#address").text("l'adresse se situe : "+address);

        $("#map")[0].src = "https://maps.googleapis.com/maps/api/staticmap?center="
                            +address+
                            "&zoom=18.5&size=600x300&maptype=roadmap&markers=color:red%7Clabel:A%7C"+
                            localization["lat"]+","+localization["lng"]+
                            "&key=AIzaSyCLNsMCYGtXdHfjbJMDRGWqY2pZkYRidbY";

        //~ $("#history").text(https://fr.wikipedia.org/w/api.php?action=opensearch&search=address&format=json);
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

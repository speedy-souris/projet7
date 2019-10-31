
$(document).ready(function(){
    function answer_gp(response){
        $('.home').hide();
        $('#gp_reply').show();
        $('#answer').show();
        //~ $('#answer').text(response);
        $('#gp_reflection').hide();
        var response_json = JSON.parse(response);
        var location = response_json["result"]["geometry"]["location"];
        var address = response_json["result"]["formatted_address"];
        $('#map')[0].src = "https://maps.googleapis.com/maps/api/staticmap?center="
                            +address
                            +"&zoom=13&size=600x380&maptype=roadmap&markers=color:red%7Clabel:A%7C"
                            +location['lat']+","+location['lng']+"&key=AIzaSyCLNsMCYGtXdHfjbJMDRGWqY2pZkYRidbY";
    };
    $('#submit2').submit(function(e){

    /*
     *send a question to GrandPy
    */
        $('.home').hide();
        $('#gp_reflection').show();
        $.ajax({
            url: '/index/2/' + $('#question').val().toString(),
            type: 'GET',
            dataType: 'html',
            success: answer_gp
        });
        e.preventDefault();
    });

});

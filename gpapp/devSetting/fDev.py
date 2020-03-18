#coding:utf-8
#!/usr/bin/env python

import json
import urllib.request, urllib.parse
# ~ from .. import question_answer as script
from .dataRedis import Conversation
# ~ from . import dataMap as map
from .dataInitial import InitData

#==================================
# Initialization status parameters
#==================================
def initial_status():
    """
        creation and initialization of parameters for REDIS
    """
    setting = Conversation()

    setting.writeQuotas(False)
    setting.writeCivility(False)
    setting.writeDecency(True)
    setting.writeComprehension(True)
    setting.writeCounter()

#================================
# address coordinate calculation
#================================
def map_coordinates(question):
    """
        calculating the coordinates of the question asked to granbpy
        Vars :
            - parser_answer
            - place_id_dict
            - map_status
    """

    # keyword isolation for question
    parse_answer = script.ApiParams().parser(question=question)

    place_id_dict = script.ApiParams().get_place_id_list(
        address=" ".join(parse_answer)
    )
    # creation and test public key api google map
    place_id = place_id_dict["candidates"][0]["place_id"]
    # creation of api google map coordinate address display setting
    # and wikipedia address history display setting
    instance()["data"].DATAMAP.address_map(
        script.ApiParams().get_address(
            place_id=place_id
        )
    )
    data.DATAMAP.history_map(
        script.ApiParams().get_history(
            search_history=" ".join(parse_answer)
        )
    )

def user_exchange(question):
    """
        user / grandpy display initialization
    """
    # politeness check
    script.Behaviour().wickedness(question)
    # courtesy check
    script.Behaviour().civility(question)
    # comprehension check
    script.Behaviour().comprehension(question)
    # end of session check
    if setting.DataRedis().readCounter() >= 10:
        setting.DataRedis().writeQuotas(True)
        setting.DataRedis().expiryCounter()
    script.Behaviour().counter_session(question, setting.DataRedis().readCounter())
    script.Behaviour().apiSession(question)

# ~ def debug():
    # ~ """
        # ~ debugging function for value and import verification
    # ~ """
    # ~ dbg_import = {
        # ~ "name_redis": setting.DataRedis.__name__,
        # ~ "name_map": map.DataMap.__name__,
    # ~ }
    # ~ return dbg_import

#===================================
# place_id search on Google Map API
#===================================
def get_place_id_list(address):
    """
        Google map API place_id search function
    """
    key = InitData().status_env["map"] # environment variable
    # replacing space by "% 20" in the string of characters
    address_encode = urllib.parse.quote(address)

    place_id = urllib.request.urlopen(
        "https://maps.googleapis.com/maps/api/place/findplacefromtext/"\
        +f"json?input={address_encode}&inputtype=textquery&key={key}"
    )

    result = json.loads(place_id.read().decode("utf8"))

    return result

#===========================
# address on Google Map API
#===========================
def get_address(place_id):
    """
        Google map API address search with place_id function
    """
    key = InitData().status_env["map"] # environment variable

    address_found= urllib.request.urlopen(
        "https://maps.googleapis.com/maps/api/place/details/"\
        f"json?placeid={place_id}&fields=formatted_address,geometry&key={key}"
    )

    result = json.loads(address_found.read().decode("utf8"))

    return result

#=================================
# history search on wikimedia API
#=================================
def get_history(search_history):
    """
        wikipedia API (Wikimedia) history search
    """

    # replacing space by "% 20" in the string of characters
    history_encode = urllib.parse.quote(search_history)

    history_found = urllib.request.urlopen(
        "https://fr.wikipedia.org/w/api.php?action=opensearch&search="\
        f"{history_encode}&format=json"
    )

    result = json.loads(history_found.read().decode("utf8"))
    return result

#=========================================
# map display in the Google Map Satic API
#=========================================
def get_map_static(location_map):
    """
        function of displaying the geolocation of the address
        asked to grandpy on the map of the Google Map Static API
    """
    key = InitData().status_env["staticMap"]  # environment variable

    # replacing space by "% 20" in the string of characters
    formatting_address = urllib.parse.quote(location_map["address"])
    # longitude and latitude display
    localization = location_map["location"]
    # display map
    display_map = "https://maps.googleapis.com/maps/api/staticmap?center="\
        +formatting_address+\
        "&zoom=18.5&size=600x300&maptype=roadmap&markers=color:red%7Clabel:A%7C"\
        +str(localization['lat'])+","+str(localization['lng'])+f"&key={key}"

    return display_map



#========================
# map coordinate display
#========================
# ~ def map_display():
    # ~ """
        # ~ display calculated coordinates for the map
        # ~ Vars:
            # ~ - display_map
    # ~ """
    # ~ # display parameter map of requested coordinates


    # ~ # response parameter to send
    # ~ return script.get_map_static(
        # ~ data.address_map["result"]["geometry"]["location"]()
    # ~ )
if __name__ == "__main__":
    pass



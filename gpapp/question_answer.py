#coding:utf-8
#!/usr/bin/env python

import os
import json

import urllib.request, urllib.parse
from config.parameter import production
from config.parameter import default
from config.parameter import testing
from config.parameter import constant

#==============================
# environment variable
#==============================
def var_env():
    """
        environment variable management function

            - call function of the Key_API_MAP / key_API_STATIC_MAP
            local environments variables (API key)

            - call function of the HEROKU_API_MAP / HEROKU_API_STATIC_MAP
            cloud environments variables (API key)

            - Key_API_MAP
            - Key_STATIC_MAP


    """
    api_key = {
        "map": {
            "key_API_MAP": os.getenv(
                production.env_dev["Key_API_MAP"],
                default = defaut.env_dev["Key_API_MAP"]
            )
        },
        "staticMap": {
            "key_API_STATIC_MAP": os.getenv(
                production.env_dev["key_API_STATIC_MAP"],
                default = default.env_dev["key_API_STATIC_MAP"]
            )
        }
    }

    return api_key

#==============================
# parser
#==============================
def parser(question=testing.test_data["question"]):
    """
        function that cuts the string of characters (question asked to GrandPy)
        into a word list then delete all unnecessary words to keep only
        the keywords for the search
    """

    # list of words to remove in questions
    list_question = question.split()
    unnecessary = constant.UNNECESSARY
    result = [w for w in list_question if w.lower() not in unnecessary]

    return result

#------------------------
# place_id search on Google Map API
def get_place_id_list(
    address=testing.test_data["addressPlace"]):
    """
        Google map API place_id search function
    """

    key = var_env()["map"] # environment variable

    # replacing space by "% 20" in the string of characters
    address_encode = urllib.parse.quote(address)

    place_id = urllib.request.urlopen(
        "https://maps.googleapis.com/maps/api/place/findplacefromtext/"\
        +f"json?input={address_encode}&inputtype=textquery&key={key}"
    )

    result = json.loads(place_id.read().decode("utf8"))

    return result

#------------------------
# place_id search on Google Map API
def get_address(place_id=testing.test_data["placeId"]):
    """
        Google map API address search with place_id function
    """

    key = var_env()["map"] # environment variable

    address_found= urllib.request.urlopen(
        "https://maps.googleapis.com/maps/api/place/details/"\
        f"json?placeid={place_id}&fields=formatted_address,geometry&key={key}"
    )

    result = json.loads(address_found.read().decode("utf8"))

    return result

#------------------------
# history search on wikimedia API
def get_history(search_history=testing.test_data["history"]):
    """
        wikipedia API (Wikimedia) history search
    """

    # replacing space by "% 20" in the string of characters
    history_encode = urllib.parse.quote(search_history)

    history_found= urllib.request.urlopen(
        "https://fr.wikipedia.org/w/api.php?"\
        f"action=opensearch&search={history_encode}&format=json"
    )

    result = json.loads(history_found.read().decode("utf8"))

    return result

#------------------------
# map display in the Google Map Satic API
def get_map_static(location_map):
    """
        function of displaying the geolocation of the address
        asked to grandpy on the map of the Google Map Static API
    """
    key = var_env()["staticMap"]  # environment variable

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


if __name__ == "__main__":
    pass

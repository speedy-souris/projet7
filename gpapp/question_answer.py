#coding:utf-8
#!/usr/bin/env python

import os
import json

import urllib.request, urllib.parse
from .initial import config as conf

#==============================
# parser
#==============================
def parser(question=conf.testing["question"]):
    """
        function that cuts the string of characters (question asked to GrandPy)
        into a word list then delete all unnecessary words to keep only
        the keywords for the search
    """

    # list of words to remove in questions
    list_question = question.split()
    unnecessary = conf.constant["unnecessary"]
    result = [w for w in list_question if w.lower() not in unnecessary]

    return result

#------------------------
# place_id search on Google Map API
def get_place_id_list(address=conf.testing["addressPlace"]):
    """
        Google map API place_id search function
    """

    key = conf.status_env # environment variable

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
def get_address(place_id=conf.testing["placeId"]):
    """
        Google map API address search with place_id function
    """

    key = conf.status_env # environment variable

    address_found= urllib.request.urlopen(
        "https://maps.googleapis.com/maps/api/place/details/"\
        f"json?placeid={place_id}&fields=formatted_address,geometry&key={key}"
    )

    result = json.loads(address_found.read().decode("utf8"))

    return result

#------------------------
# history search on wikimedia API
def get_history(search_history=conf.testing["search"]):
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
    key = conf.status_env  # environment variable

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

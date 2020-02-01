#coding:utf-8
#!/usr/bin/env python

import json
import urllib.request, urllib.parse
from .initial import Parameter as config
from .classSetting import DataSetting as setting
from . import question_answer

class ParamsDefault:
    """
        management of API parameters
    """
    def __init__(self):
        self.data = {}

class Params:
    """
        API default settings for testing
    """
    DATA = ParamsDefault()

    @classmethod
    def data_test(cls):
        """
            Initialization of API parameters by default for tests
        """
        cls.DATA.data["placeId"] = "ChIJTei4rhlu5kcRPivTUjAg1RU"
        cls.DATA.data["question"] = "ou se trouve la poste de marseille"
        cls.DATA.data["addressPlace"] = "paris poste"
        cls.DATA.data["search"] = "montmartre"

        return cls.DATA.data

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
    parse_answer = question_answer.parser(question = question)
    place_id_dict = question_answer.get_place_id_list(
        address = " ".join(parse_answer)
    )
    # creation and test public key api google map
    place_id = place_id_dict["candidates"][0]["place_id"]
    # creation of api google map coordinate address display setting
    # and wikipedia address history display setting
    setting.address_map(
        question_answer.get_address(
            place_id = place_id
        )
    )
    setting.history_map(
        question_answer.get_history(
            search_history = " ".join(parse_answer)
        )
    )

#========
# parser
#========
def parser(question=Params.data_test()["question"]):
    """
        function that cuts the string of characters (question asked to GrandPy)
        into a word list then delete all unnecessary words to keep only
        the keywords for the search
    """

    # list of words to remove in questions
    list_question = question.split()
    result = [
        w for w in list_question if w.lower() not in config.constant()[
            "list_unnecessary"
        ]
    ]

    return result

#===================================
# place_id search on Google Map API
#===================================
def get_place_id_list(address = Params.data_test()["addressPlace"]):
    """
        Google map API place_id search function
    """

    key = config.status_env()["map"] # environment variable
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
def get_address(place_id=Params.data_test()["placeId"]):
    """
        Google map API address search with place_id function
    """
    key = config.status_env()["map"] # environment variable
    address_found= urllib.request.urlopen(
        "https://maps.googleapis.com/maps/api/place/details/"\
        f"json?placeid={place_id}&fields=formatted_address,geometry&key={key}"
    )

    result = json.loads(address_found.read().decode("utf8"))

    return result

#=================================
# history search on wikimedia API
#=================================
def get_history(search_history=Params.data_test()["search"]):
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
    key = config.status_env()["staticMap"]  # environment variable

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

#===========================
# Initialization wickedness
#===========================
def wickedness(question):
    """
        Disrespect management function
        initialization of wickedness
            - decency
     """
    if question.lower() in config.constant()["list_indecency"]:
        setting.writeDecency(False)
    return setting.readDecency()

#=========================
# Initialization Civility
#=========================
def civility(question):
    """
        Incivility management function
        initialization of incivility
            - civility
    """
    if question.lower() in config.constant()["list_civility"]:
        setting.writeCivility(True)
    return setting.readCivility()

#==============================
# Initialization comprehension
#==============================
def comprehension(question):
    """
        Incomprehension management function
        initialization of incomprehension
            - comprehension
    """
    try:
        map_coordinates(question)
    except IndexError:
        setting.writeComprehension(False)

    return setting.readComprehension()


if __name__ == "__main__":
    pass

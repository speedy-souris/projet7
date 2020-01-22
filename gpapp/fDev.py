#coding:utf-8
#!/usr/bin/env python

from .question_answer import parser
from .question_answer import get_address, get_place_id_list
from .question_answer import get_map_static
from .question_answer import get_history
from .classRedis import DataSetting as setting
from .initial import Parameter as config

#==========================
# Initialization status parameters
#==========================
def initial_status():
    """
        creation and initialization of parameters for REDIS
    """
    setting.writeQuotas(False)
    setting.writeCivility(False)
    setting.writeDecency(True)
    setting.writeComprehension(True)
    setting.writeCounter()

#============================
# Initialization Map Status
#============================
def map_status():
    """
        initialization of the default settings
        for displaying the map (grandpy response)
    """
    map_status = {
        "address": "",
        "history": ""
    }
    return map_status

#===========================
# Initialization wickedness
#===========================
def wickedness(question):
    """
        Disrespect management function
        initialization of wickedness
            - decency
     """
    # ~ parameter_status = data["parameter_status"]

    if question.lower() in config.constant()["list_indecency"]:
        setting.writeDecency(False)
    return setting.readDecency()

#=========================
# Initialization Civility
#=========================
def incivility(question):
    """
        Incivility management function
        initialization of incivility
            - civility
    """
    if question.lower() in config.constant()["list_civility"]:
        setting.writeCivility(True)
    return setting.readCivility()

#================================
# address coordinate calculation
#================================
def map_coordinates(data):
    """
        calculating the coordinates of the question asked to granbpy
        Vars :
            - parser_answer
            - place_id_dict
            - map_status
    """
    map_status = data["map_status"]
    # keyword isolation for question
    parse_answer = parser(question = data["question"])
    place_id_dict = get_place_id_list(address = " ".join(parse_answer))
    # creation and test public key api google map
    place_id = place_id_dict["candidates"][0]["place_id"]
    # creation of api google map coordinate address display setting
    # and wikipedia address history display setting

    map_status["address"] = get_address(place_id = place_id)



    map_status["history"] = get_history(
        search_history = " ".join(parse_answer)
    )
    # ~ map_status["data_map"]["address"] =\
        # ~ map_status["address"]["result"]["formatted_address"]
    # ~ map_status["data_map"]["location"] =\
        # ~ map_status["address"]["result"]["geometry"]["location"]

    # Display of the map according to the requested coordinates
    try:
        map_status["address"]
    except KeyError:
        setting.writeQuotas(True)
        return setting.readQuotas()

    return map_status

#========================
# map coordinate display
#========================
def map_display(data):
    """
        display calculated coordinates for the map
        Vars:
            - display_map
    """
    map_status = data["map_status"]
    print(map_status)
    # display parameter map of requested coordinates
    display_map = get_map_static(map_status["data_map"])
    map_status["display_map"] = display_map
    # response parameter to send
    return map_status

#coding:utf-8
#!/usr/bin/env python

from . import question_answer
from .classSetting import DataSetting as setting
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
    address = setting.address_map(question_answer.get_address(place_id = place_id))

    history = setting.history_map(question_answer.get_history(
        search_history = " ".join(parse_answer))
    )
    # Display of the map according to the requested coordinates
    try:
        address
    except KeyError:
        setting.writeQuotas(True)
        return setting.readQuotas()
    print(setting.response((address, history)))
    return setting.response((address, history))

#========================
# map coordinate display
#========================
def map_display():
    """
        display calculated coordinates for the map
        Vars:
            - display_map
    """
    # display parameter map of requested coordinates


    # response parameter to send
    return question_answer.get_map_static(
        setting.address_map["result"]["geometry"]["location"]()
    )

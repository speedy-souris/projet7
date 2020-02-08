#coding:utf-8
#!/usr/bin/env python

import time
from .. import question_answer as script
from .. import views as reset
from ..classSetting.dataRedis import DataRedis as setting
from ..classSetting.dataMap import DataMap as data


#==================================
# Initialization status parameters
#==================================
def initial_status():
    """
        creation and initialization of parameters for REDIS
    """
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
    parse_answer = script.parser(question = question)
    place_id_dict = script.get_place_id_list(
        address = " ".join(parse_answer)
    )
    # creation and test public key api google map
    place_id = place_id_dict["candidates"][0]["place_id"]
    # creation of api google map coordinate address display setting
    # and wikipedia address history display setting
    data.address_map(
        script.get_address(
            place_id = place_id
        )
    )
    data.history_map(
        script.get_history(
            search_history = " ".join(parse_answer)
        )
    )

def user_exchange(question):
    """
        user / grandpy display initialization
    """
    # politeness check
    script.wickedness(question)
    # courtesy check
    script.civility(question)
    # comprehension check
    script.comprehension(question)
    # end of session check
    if setting.readCounter() >= 10:
        setting.writeQuotas(True)
        setting.expiryCounter()
    script.counter_session(question, setting.readCounter)
    script.apiSession(question)

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


#coding:utf-8
#!/usr/bin/env python

import json
import urllib.request, urllib.parse
from .. import question_answer as script
import devSetting.dataRedis
# ~ from . import dataMap as map
from .dataInitial import InitData

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



if __name__ == "__main__":
    pass



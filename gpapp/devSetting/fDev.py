#coding:utf-8
#!/usr/bin/env python

# ~ from .. import question_answer
from dataRedis import DataRedis
from dataMap import DataMap

def instance():
    """
        creation of instances for imported classes
    """
    self.inst = {
        "setting": DataRedis(),
        "script": question_answer(),
        "data": DataMap()
    }
#==================================
# Initialization status parameters
#==================================
def initial_status():
    """
        creation and initialization of parameters for REDIS
    """
    instance()["setting"].writeQuotas(False)
    instance()["setting"].writeCivility(False)
    instance()["setting"].writeDecency(True)
    instance()["setting"].writeComprehension(True)
    instance()["setting"].writeCounter()

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
    parse_answer = instance()["script"].ApiParams().parser(question=question)
    place_id_dict = instance()["script"].ApiParams().get_place_id_list(
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
    print(setting.DataRedis().readCounter())


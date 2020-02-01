#coding:utf-8
#!/usr/bin/env python


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



    # ~ address = setting.address_map(question_answer.get_address(place_id = place_id))
    # ~ address = address["address"]["result"]
    # ~ history = setting.history_map(question_answer.get_history(
        # ~ search_history = " ".join(parse_answer))

    # Display of the map according to the requested coordinates
    # ~ return question_answer.get_history(
        # ~ search_history = " ".join(parse_answer)
    # ~ )

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
if __name__ == "__main__":
    pass


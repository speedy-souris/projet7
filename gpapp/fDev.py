#coding:utf-8
#!/usr/bin/env python

from . import question_answer
from .classSetting import DataSetting as setting
from .initial import Parameter as config



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


#coding:utf-8
#!/usr/bin/env python

import time
from flask import Flask, render_template
# ~ import devSetting
# ~ import gpapp
from .devSetting import dataRedis as setting

from .devSetting import dataMap as data
from .devSetting import fDev as func
# ~ import question_answer as script

app = Flask(__name__)

#======================================
# main function for displaying answers
#======================================
@app.route("/")
def index():
    """
        Initialization of the index.html page
        single home page
    """
    if setting.DataRedis().read_quotas and setting.DataRedis().read_counter == 0:
        func.initial_status()
    return render_template("index.html")

# ~ # Initialization of general parameters
@app.route("/index/<reflection>/<question>")
def answer_gp(reflection, question):
    """
        grandpy's response display function
        setting the parameter for grandpy's responses
        general variable to count grandpy's responses
        and the state of civility in the questions
        as well as the different coordinates for the display of the map
            - quotas_api
            - civility
            - decency
            - nb_request
            - comprehension
            - address (answer and data map)
            - history
            - location
    """
    if setting.DataRedis().read_quotas:
        func.initial_status()
    # grandpy's reflection time to answer questions
    time_reflection = time.sleep(int(reflection))
    # exchange between the user and grandpy
    func.user_exchange(question)
    # sending parameters
    data_send = {
        "parameter_status": {
            "quotas_api": setting.DataRedis().read_quotas,
            "nb_request": setting.DataRedis().read_counter,
            "civility": setting.DataRedis().read_civility,
            "decency": setting.DataRedis().read_decency,
            "comprehension": setting.DataRedis().read_comprehension
        },
        "map_status": data.DataMap().data_map().get("address", ""),
        "wiki_status": data.dataMap().data_map().get("history", "")
    }
    return data_send


if __name__ == "__main__":
    pass

#coding:utf-8
#!/usr/bin/env python

import time
from flask import Flask, render_template
from .classSetting.dataRedis import DataRedis as setting
from .classSetting.dataMap import DataMap as data
from .funcDev import fDev as func
from . import question_answer as script

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
    if setting.readQuotas() and setting.readCounter == 0:
        func.initial_status()
    return render_template("index.html")

# Initialization of general parameters
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
    if setting.readQuotas():
        func.initial_status()
    # grandpy's reflection time to answer questions
    time_reflection = time.sleep(int(reflection))
    # exchange between the user and grandpy
    func.user_exchange(question)
    # sending parameters
    data_send = {
        "parameter_status": {
            "quotas_api": setting.readQuotas(),
            "nb_request": setting.readCounter(),
            "civility": setting.readCivility(),
            "decency": setting.readDecency(),
            "comprehension": setting.readComprehension()
        },
        "map_status": data.readResponse().get("address", ""),
        "wiki_status": data.readResponse().get("history", "")
    }
    return data_send

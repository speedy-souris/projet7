#coding:utf-8
#!/usr/bin/env python

import time
from flask import Flask, render_template
from . import fDev
from .classSetting import DataSetting as setting
from . import question_answer

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
    if setting.readQuotas():
        fDev.initial_status()
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
        fDev.initial_status()
    # grandpy's reflection time to answer questions
    time_reflection = time.sleep(int(reflection))
    # politeness check
    question_answer.wickedness(question)
    # courtesy check
    if not setting.readCivility():
        question_answer.civility(question)
    # coordinate calculation
    if question_answer.comprehension(question):
        setting.incrementCounter()
    # control of the display of map coordinates
    if setting.readCounter() >= 10:
        setting.writeQuotas(True)
        setting.expiryCounter()
    # sending parameters
    data_send = {
        "parameter_status": {
            "nb_request": setting.readCounter(),
            "civility": setting.readCivility(),
            "decency": setting.readDecency(),
            "comprehension": setting.readComprehension()
        },
        "map_status": setting.readResponse()["address"],
        "wiki_status": setting.readResponse()["history"]
    }
    return data_send

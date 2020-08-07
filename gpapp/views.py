#coding:utf-8
#!/usr/bin/env python

import time
from flask import Flask, render_template
# ~ import devSetting
# ~ import gpapp
from .blending import instantiation as dialog
from .blending import main

# ~ from .devSetting import dataMap as data
# ~ from .devSetting import fDev as func
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
    if dialog.read_quotas and dialog.read_counter == 0:
        dialog.initial_status()
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
    if dialog.read_quotas:
        dialog.initial_status()
    # grandpy's reflection time to answer questions
    time_reflection = time.sleep(int(reflection))
    # exchange between the user and grandpy
    main()
    # sending parameters
    data_send = {
        "parameter_status": {
            "quotas_api": dialog.read_quotas,
            "nb_request": dialog.read_counter,
            "civility": dialog.read_civility,
            "comprehension": dialog.read_comprehension
        },
        # ~ "map_status": data.DataMap().data_map().get("address", ""),
        # ~ "wiki_status": data.dataMap().data_map().get("history", "")
    }
    print(f"parmetre status ==> {data_send}")
    return data_send


if __name__ == "__main__":
    pass

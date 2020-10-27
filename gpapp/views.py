#coding:utf-8
#!/usr/bin/env python

import time
from flask import Flask, render_template

from .parameter import QuestionParameter
from .process import Processing
from .main import main

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
    if QuestionParameter.read_quotas and QuestionParameter.read_counter == 0:
        QuestionParameter.initial_status()
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
    if QuestionParameter.read_quotas:
        QuestionParameter.initial_status()
    # grandpy's reflection time to answer questions
    time_reflection = time.sleep(int(reflection))
    # exchange between the user and grandpy
    main()
    # sending parameters
    data_send = {
        "parameter_status": {
            "quotas_api": QuestionParameter.read_quotas,
            "nb_request": QuestionParameter.read_counter,
            "civility": QuestionParameter.read_civility,
            "comprehension": QuestionParameter.read_comprehension
        },
        "map_status": Processing.map_coordinates.get("address", ""),
        "wiki_status": Processing.map_coordinates.get("history", "")
    }
    print(f"parmetre status ==> {data_send}")
    return data_send


if __name__ == "__main__":
    pass

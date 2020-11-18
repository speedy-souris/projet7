#coding:utf-8
#!/usr/bin/env python

import time
from flask import Flask, render_template

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
    # grandpy's reflection time to answer questions
    time_reflection = time.sleep(int(reflection))
    # exchange between the user and grandpy
    connect = main()
    print(connect.read_response())
    # sending parameters
    data_send = {
        "grandpy_response": connect.read_response(),
        # ~ "map_status": main.internal_process.map_coordinates.get("address", ""),
        # ~ "wiki_status": main.internal_process.map_coordinates.get("history", "")
    }
    print(f"parametre status ==> {data_send}")
    return data_send


if __name__ == "__main__":
    pass

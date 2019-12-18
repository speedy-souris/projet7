#coding:utf-8
#!/usr/bin/env python

import time
from flask import Flask, render_template
from .question_answer import parser as needless
from .question_answer import get_address as address
from .question_answer import get_history as wiki
from .question_answer import get_map_static as geo_location
from .config.parameter import base
from .config.parameter import constant

app = Flask(__name__)

#=============
# update data
#=============
def update_data(data):
    """
        update function of data status
    """
    return {
        "question": data[0]["question"],
        "grandpy_status": data[1]
    }

#===========================
# Initialization wickedness
#===========================
def wickedness(data):
    """
        Disrespect management function
        initialization of wickedness

            - decency
     """
    question = data[0]["question"]
    grandpy_status = data[1]
    lst_indecency = constant.LST_INDENCY

    if question.lower() in lst_indecency:
        grandpy_status["politeness"]["decency"] = False
    else:
        grandpy_status["politeness"]["decency"] = True

    return grandpy_status

#=========================
# Initialization Civility
#=========================
def incivility(data):
    """
        Incivility management function
        initialization of incivility
            - civility
    """
    question = data[0]["question"]
    grandpy_status = data[1]
    lst_civility = constant.LST_CIVILITY

    if question.lower() in lst_civility:
        grandpy_status["politeness"]["civility"] = True
        grandpy_status["nb_request"] += 1

    return grandpy_status

#================================
# address coordinate calculation
#================================
def map_coordinates(data):
    """
        calculating the coordinates of the question asked to granbpy
        Vars :

            - parser_answer
            - place_id_dict
            - grandpy_status
    """
    question = data[0]["question"]
    grandpy_status = data[1]
    # keyword isolation for question
    parse_answer = needless(question = question)
    place_id_dict = reference_id(address = " ".join(parse_answer))
    # creation and test public key api google map
    try:
        place_id = place_id_dict["candidates"][0]["place_id"]
    except IndexError:
        grandpy_status["comprehension"] = False
        return grandpy_status
    # creation of api google map coordinate address display setting
    # and wikipedia address history display setting
    grandpy_status["answer"]["address"] = address(place_id = place_id)
    grandpy_status["answer"]["history"] = wiki(
        search_history = " ".join(parse_answer)
    )
    grandpy_status["data_map"]["address"] = grandpy_status[
        "answer"]["address"]["result"]["formatted_address"]
    grandpy_status["data_map"]["location"] = grandpy_status[
        "answer"]["address"]["result"]["geometry"]["location"]
    # Display of the map according to the requested coordinates
    try:
        grandpy_status["data_map"]
    except KeyError:
        grandpy_status["over_quotas"] = True
        return grandpy_status

    return grandpy_status

#========================
# map coordinate display
#========================
def map_display(data):
    """
        display calculated coordinates for the map
        Vars:

            - display_map
            - grandpy_status
    """
    question = data[0]["question"]
    grandpy_status = data[1]
    # display parameter map of requested coordinates
    display_map = geo_location(grandpy_status["data_map"])
    grandpy_status["display_map"] = display_map
    # counting answer grandpy
    if grandpy_status["nb_request"] == 10:
        grandpy_status["over_quotas"] = True

    # response parameter to send
    return grandpy_status


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

@app.route("/index/<reflection>/<question>")
def answer_gp(reflection, question):
    """ display function of grandpy answers
        setting up parameter for grandpy's answers
        general global variable for counting grandpy responses
        and the state of civility in questions
            - over_quotas
            - civility
            - decency
            - nb_request
    """
    # Initialization parameters
    grandpy_status = {
        "over_quotas": base.params["over_quotas"],
        "politeness": {
            "civility": base.params["politeness"]["civility"],
            "decency": base.params["politeness"]["decency"]
        },
        "comprehension": base.params["comprehension"],
        "nb_request": base.params["nb_request"],
        "answer": {
            "address": "",
            "history": ""
        },
        "data_map": {
            "address": "",
            "location": ""
        },
        "display_map": "",
    }
    data = {
        "question": question,
        "qrandpy_status": grandpy_status
    }
    # grandpy's reflection time to answer questions
    time_reflection = time.sleep(int(reflection))
    nastiness = wickedness(data)
    grandpy_status = nastiness
    data = update_data((data,grandpy_status))

    if not grandpy_status["politeness"]["civility"]:
        courtesy = incivility(data)
    grandpy_status = courtesy
    data = update_data((data,grandpy_status))

    # coordinate calculation
    data_status = map_coordinates(data)
    grandpy_status = data_status
    data = update_data((data,grandpy_status))

    try:
        # map coordinate display
        coordonate_map = map_display(data)
    except TypeError:
        grandpy_status["comprehension"] = False
        return grandpy_status

    grandpy_status = coordonate_map

    if grandpy_status["politeness"]["civility"]:
        grandpy_status["nb_request"] += 1

    return grandpy_status











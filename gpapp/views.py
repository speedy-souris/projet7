#coding:utf-8
import time

from flask import Flask, render_template, request

from . import question_answer

app = Flask(__name__)

#-------------------
# global politeness
# and question count parameter
parameter_answer = {
    "politeness": {
        "civility": False,
        "decency": True
    },
    "counter_answer": 0
}

#---------------------------
# incivility in the question
def civility(question):
    """Incivility management function"""
    global parameter_answer
    lst_civility = [
        "bonjour grandpy","bonsoir grandpy","salut grandpy",
        "hello grandpy","bonjour grandPy comment vas tu",
        "comment allez vous grandpy","salut grandpy comment ca va"
        "bonjour", "bonsoir","salut","hello"
    ]
    if question in lst_civility:
        parameter_answer["politeness"]["civility"] = True


#------------------------
# disrespect in the question
def wickedness(question):
    """Disrespect management function"""
    lst_indecency = [
        "salut vieux poussierieux","salut ancetre demode","salut vieillard senille",
        "salut dinosaure decrepit","salut arriere rococo","salut centenaire senille",
        "salut vieillot archaique","salut vieux","salut vieux gateux","salut vieux croulant",
        "salut antiquite","salut vieille baderne","salut vieux fossile",
        "bonjour vieux poussierieux","bonjour ancetre demode","bonjour vieillard senille",
        "bonjour dinosaure decrepit","bonjour arriere rococo","bonjour centenaire senille",
        "bonjour vieillot archaique","bonjour vieux","bonjour vieux gateux","bonjour vieux croulant",
        "bonjour antiquite","bonjour vieille baderne","bonjour vieux fossile",
        "bonsoir vieux poussierieux","bonsoir ancetre demode","bonsoir vieillard senille",
        "bonsoir dinosaure decrepit","bbonsoir arriere rococo","bonsoir centenaire senille",
        "bonsoir vieillot archaique","bonsoir vieux","bonsoir vieux gateux","bonsoir vieux croulant",
        "bonsoir antiquite","bonsoir vieille baderne","bonsoir vieux fossile",
        "vieux poussierieux","ancetre demode","vieillard senille",
        "dinosaure decrepit","arriere rococo","centenaire senille",
        "vieillot archaique","vieux","vieux gateux","vieux croulant",
        "antiquite","vieille baderne","vieux fossile"
    ]
    if question in lst_indecency:
        parameter_answer["politeness"]["decency"] = False
    else:
        parameter_answer["politeness"]["decency"] = True

#---------------------------
# Display of grandpy's answer
# (address, map, wiki and personal anectode)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index/<reflection>/<question>")
def answer_gp(reflection, question):
    """ display function of grandpy answers
        setting up parameter for grandpy's answers

        general global variable for counting grandpy responses
        and the state of civility in questions
            - parameter_answer

        general settings for grandpy responses
            - grandpy_status
    """
    # parameter for grandpy's answers
    global parameter_answer
    grandpy_status = {
        "quotas_api": {
            "over_quotas": False,
            "comprehension": True,
        },
        "answer": {
            "address": "",
            "history": ""
        },
        "data_map": {
            "address": "",
            "location": ""
        }
    }

    # grandpy's reflection time to answer questions
    time_reflection = time.sleep(int(reflection))

    # management incivility and disrespect
    wickedness(question)
    if parameter_answer["politeness"]["civility"] == False:
        civility(question)

    # keyword isolation for question
    parse_answer = question_answer.parser(question = question)
    place_id_dict = question_answer.get_place_id_list(address = " ".join(parse_answer))

    # creation and test public key api google map
    try:
        place_id = place_id_dict["candidates"][0]["place_id"]
    except IndexError:
        grandpy_status["quotas_api"]["comprehension"] = False
        response = {
            "quotas_api": grandpy_status["quotas_api"],
            "politeness": parameter_answer["politeness"]
        }
        return response

    # creation of api google map coordinate address display setting
    # and wikipedia address history display setting
    grandpy_status["answer"]["address"] = question_answer.get_address(place_id = place_id)
    grandpy_status["answer"]["history"] = question_answer.get_history(
        search_history = " ".join(parse_answer)
    )
    address = grandpy_status["answer"]["address"]

    # Display of the map according to the requested coordinates
    try:
        grandpy_status["data_map"]["address"] = address["result"]["formatted_address"]
        grandpy_status["data_map"]["location"] = address["result"]["geometry"]["location"]
    except KeyError:
        grandpy_status["quotas_api"]["over_quotas"] = True
        response = {
            "answer": grandpy_status["answer"],
            "quotas_api": grandpy_status["quotas_api"],
            "politeness": parameter_answer["politeness"]
        }
        return response

    # display parameter map of requested coordinates
    display_map = question_answer.get_map_static(grandpy_status["data_map"])

    # counting answer grandpy
    if parameter_answer["counter_answer"] < 10:
        if parameter_answer["politeness"]["civility"]:
            parameter_answer["counter_answer"] += 1
        else:
            parameter_answer["counter_answer"] = 0
    else:
        grandpy_status["quotas_api"]["over_quotas"] = True

    # response parameter to send
    response = {
        "answer": grandpy_status["answer"],
        "quotas_api": grandpy_status["quotas_api"],
        "politeness": parameter_answer["politeness"],
        "nb_response": parameter_answer["counter_answer"],
        "display_map": display_map
    }
    return response

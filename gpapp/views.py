#coding:utf-8
import time
from flask import Flask, render_template, request
from . import question_answer

app = Flask(__name__)

#===============================
# Parameter and Quotas API
#===============================
PARAMETER = {
    "OVER_QUOTAS": False,
    "NB_REQUEST": 0,
    "CIVILITY": False,
    "DECENCY": True
}
#==============================
# Parameter for politenes
#==============================
class Politeness:
    """
        politeness management class for persona (grandpy)
        Initialization of civility with "incivility" property
        Initialisation of indecency with "wickedness" property

        Args for Politeness class :

            - civility
            - dencency
            - question

        Vars Params for Politeness class :

            - LST_CIVILITY ==> preferable civility
                                at the first contact for the persona character

            - LST_INDECENCY ==> avoid the lack of courtesy towards the persona
    """
    global PARAMETER  # loading parameter for incivility and wickedness
    # list for politeness and respect for the persona
    LST_CIVILITY = [
        "bonjour grandpy","bonsoir grandpy","salut grandpy",
        "hello grandpy","bonjour grandPy comment vas tu",
        "comment allez vous grandpy","salut grandpy comment ca va"
        "bonjour", "bonsoir","salut","hello"
    ]
    LST_INDECENCY = [
        "salut vieux","salut vieux con","salut vieux poussierieux",
        "salut ancetre demode","salut vieillard senille","salut dinosaure decrepit",
        "salut arriere rococo","salut centenaire senille","salut vieillot archaique",
        "salut vieux","salut vieux gateux","salut vieux croulant","salut antiquite",
        "salut vieille baderne","salut vieux fossile","bonjour vieux",
        "bonjour vieux con","bonjour vieux poussierieux","bonjour ancetre demode",
        "bonjour vieillard senille","bonjour dinosaure decrepit",
        "bonjour arriere rococo","bonjour centenaire senille",
        "bonjour vieillot archaique","bonjour vieux","bonjour vieux gateux",
        "bonjour vieux croulant","bonjour antiquite","bonjour vieille baderne",
        "bonjour vieux fossile","bonsoir vieux poussierieux","bonsoir ancetre demode",
        "bonsoir vieillard senille","bonsoir dinosaure decrepit",
        "bonsoir arriere rococo","bonsoir centenaire senille",
        "bonsoir vieillot archaique","bonsoir vieux","bonsoir vieux gateux",
        "bonsoir vieux croulant","bonsoir antiquite","bonsoir vieille baderne",
        "bonsoir vieux fossile","sale vieux","vieux con","vieux poussierieux",
        "ancetre demode","vieillard senille","dinosaure decrepit","arriere rococo",
        "centenaire senille","vieillot archaique","vieux gateux","vieux croulant",
        "antiquite","vieille baderne","vieux fossile"
    ]
                        #============================
                        # Initialisazion Parameters
                        #============================

    def __init__(self, question):
        """
            Initialization of incivility / decency (by default))
            initialization of question (for grandPy)

                - civility
                - decency
                - question

        """
        self.civility = PARAMETER["CIVILITY"]
        self.decency  = PARAMETER["DECENCY"]
        self.question = question

                        #============================
                        # Initialisazion Civility
                        #============================

    @property
    def incivility(self):
        """
            Incivility management function
            initialization of incivility

                - civility
        """
        global PARAMETER  # loading parameter for incivility

        lst_civility = self.LST_CIVILITY
        if self.question in lst_civility:
            PARAMETER["CIVILITY"] = True
            PARAMETER["NB_REQUEST"] += 1

                        #============================
                        # Initialisazion wickedness
                        #============================
    @property
    def wickedness(self):
        """
            Disrespect management function
            initialization of wickedness

                - decency
        """
        global PARAMETER   # loading parameter for wickedness

        lst_indecency = self.LST_INDECENCY
        if self.question in lst_indecency:
            PARAMETER["DECENCY"] = False

        else:
            PARAMETER["DECENCY"] = True

#==============================
# address coordinate calculation
#==============================
def map_coordinates(question, grandpy_status):

    global PARAMETER    # loading parameter for updating data
    # keyword isolation for question
    parse_answer = question_answer.parser(question = question)
    place_id_dict = question_answer.get_place_id_list(
        address = " ".join(parse_answer)
    )
    # creation and test public key api google map
    try:
        place_id = place_id_dict["candidates"][0]["place_id"]
    except IndexError:
        grandpy_status["comprehension"] = False

        return grandpy_status
    # creation of api google map coordinate address display setting
    # and wikipedia address history display setting
    grandpy_status["answer"]["address"] = question_answer.get_address(
        place_id = place_id
    )
    grandpy_status["answer"]["history"] = question_answer.get_history(
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
        PARAMETER ["OVER_QUOTAS"] = True
        grandpy_status["quotas_api"] = PARAMETER ["OVER_QUOTAS"]

        return grandpy_status

    return grandpy_status

#==============================
# map coordinate display
#==============================
def map_display(question, grandpy_status):

    global PARAMETER    # loading parameter for updating data
    # display parameter map of requested coordinates
    display_map = question_answer.get_map_static(grandpy_status["data_map"])
    grandpy_status["display_map"] = display_map
    # counting answer grandpy
    if PARAMETER["NB_REQUEST"] == 10:
        PARAMETER ["OVER_QUOTAS"] = True
        grandpy_status["quotas_api"] = PARAMETER ["OVER_QUOTAS"]

    # response parameter to send
    return grandpy_status
#==============================

#==============================
# update data
#==============================
def update_data(grandpy_status):

    global PARAMETER

    update_status = {
        "answer": {
            "address": grandpy_status["answer"]["address"],
            "history": grandpy_status["answer"]["history"]
        },
        "comprehension": grandpy_status["comprehension"],
        "data_map": {
            "address": grandpy_status["data_map"]["address"],
            "location": grandpy_status["data_map"]["location"]
        },
        "display_map": grandpy_status["display_map"],
        "nb_request": PARAMETER["NB_REQUEST"],
        "politeness": {
            "civility": PARAMETER["CIVILITY"],
            "decency": PARAMETER["DECENCY"]
        },
        "quotas_api": PARAMETER ["OVER_QUOTAS"]
    }
    return update_status

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index/<reflection>/<question>")
def answer_gp(reflection, question):
    """ display function of grandpy answers
        setting up parameter for grandpy's answers

        general global variable for counting grandpy responses
        and the state of civility in questions

    """
    global PARAMETER

    politeness = Politeness(question)
    grandpy_status = {
        "quotas_api": PARAMETER ["OVER_QUOTAS"],
        "politeness": {
            "civility": PARAMETER["CIVILITY"],
            "decency": PARAMETER["DECENCY"]
        },
        "comprehension": True,
        "nb_request": PARAMETER["NB_REQUEST"],
        "answer": {
            "address": "",
            "history": ""
        },
        "data_map": {
            "address": "",
            "location": ""
        },
        "display_map": ""
    }
    # grandpy's reflection time to answer questions
    time_reflection = time.sleep(int(reflection))
    # management incivility and disrespect
    politeness.wickedness
    grandpy_status["politeness"]["decency"] = PARAMETER["DECENCY"]

    if not PARAMETER["CIVILITY"]:
        politeness.incivility
    grandpy_status["politeness"]["civility"] = PARAMETER["CIVILITY"]

    # coordinate calculation
    data_status = map_coordinates(question, grandpy_status)
    try:
        # map coordinate display
        coordonate_map = map_display(question, update_data(data_status))
    except TypeError:
        grandpy_status["comprehension"] = False
        return grandpy_status

    new_status = update_data(coordonate_map)

    if PARAMETER["CIVILITY"]:
        PARAMETER["NB_REQUEST"] += 1
    return new_status







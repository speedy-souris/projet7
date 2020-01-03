#coding:utf-8
#!/usr/bin/env python

import time
from flask import Flask, render_template
import redis
from .question_answer import parser
from .question_answer import get_address, get_place_id_list
from .question_answer import get_map_static
from .question_answer import get_history
from . import initial as init
from .initial import conf

app = Flask(__name__)

#=================
# Read / Write
# Data of setting
#=================
class DataSetting:
    """
        Management class for saving configuration parameters:
            - config ==> database parameter
            - quotas_api
            - civility
            - decency
            - comprehension
            - nb_request
    """
    def __init__(self):
        # ~ if conf.status_env == "HEROKU_KEY_API_MAP":
            # ~ self.config = redis2
        # ~ else:
        self.config = redis.Redis(host='localhost', port=6379, db=0)
        self.quotas_api = False
        self.civility = False
        self.decency = True
        self.comprehension = True
        self.nb_request = 0
    #-------------------------- DATA WRITING  -----------------------
    # save quotas parameter
    @property
    def write_quotas(parameter_quotas):
        """
            saving of quotas configuration
        """
        self.quotas_api = parameter_quotas["quotas_api"]
        quotas_api = self.config.set("quotas_api", self.quotas_api)
        data = {
            "quotas_api": quotas_api
        }
        return data
    # save civility parameter
    @property
    def write_civility(parameter_civility):
        """
            saving of civility configuration
        """
        self.civility = parameter_civility["civility"]
        civility = self.config.set("civility", self.civility)
        data = {
            "civility": civility
        }
        return data
    # save decency parameter
    @property
    def write_decency(parameter_decency):
        """
            saving of decency configuration
        """
        self.decency = parameter_decency["decency"]
        decency = self.config.set("decency", self.decency)
        data = {
            "decency": decency
        }
        return data
    # save comprehension parameter
    @property
    def write_comprehension(parameter_comprehension):
        """
            saving of comprehension configuration
        """
        self.comprehension = parameter_comprehension["comprehension"]
        comprehension = self.config.set("comprehension", self.comprehension)
        data = {
            "comprehension": comprehension
        }
        return data
    # save counter parameter
    @property
    def write_counter(parameter_counter):
        """
            saving of counter configuration
        """
        self.nb_request = parameter_counter["nb_request"]
        nb_request = self.config.incr(self.nb_request)
        data = {
            "nb_request": nb_request
        }
        return data
    #-------------------------- DATA READING  -----------------------
    # reading quotas parameter
    @property
    def read_quotas():
        """
            reading of quotas configuration
        """
        quotas_api = self.config.get(self.quotas_api)
        data = {
            "quotas_api": quotas_api
        }
        return data
    # reading civility parameter
    @property
    def read_civility():
        """
            reading of civility configuration
        """
        civility = self.config.get(self.civility)
        data = {
            "civility": civility
        }
        return data
    # reading decency parameter
    @property
    def read_decency():
        """
            reading of decency configuration
        """
        decency = self.config.get(self.decency)
        data = {
            "decency": decency
        }
        return data
    # reading comprehension parameter
    @property
    def read_comprehension():
        """
            reading of comprehension configuration
        """
        comprehension = self.config.get(self.comprehension)
        data = {
            "comprehension": comprehension
        }
        return data
    # reading counter parameter
    @property
    def read_counter():
        """
            reading of counter configuration
        """
        nb_request = self.config.get(self.nb_request)
        data = {
            "nb_request": nb_request
        }
        return data

data_config = DataSetting()

#===========================
# Initialization wickedness
#===========================
def wickedness(data):
    """
        Disrespect management function
        initialization of wickedness
            - decency
     """
    parameter_status = data["parameter_status"]

    if data["question"].lower() in conf.constant["lst_indecency"]:
        parameter_status["decency"] = False
    else:
        parameter_status["decency"] = True

    # save parameter
    data_config.write_decency(parameter_status)

#=========================
# Initialization Civility
#=========================
def incivility(data):
    """
        Incivility management function
        initialization of incivility
            - civility
    """
    parameter_status = data["parameter_status"]

    if data["question"].lower() in conf.constant["lst_civility"]:
        parameter_status["civility"] = True
    # save parameter
    civility = data_config.write_civility(parameter_status)
    return civility

#================================
# address coordinate calculation
#================================
def map_coordinates(data):
    """
        calculating the coordinates of the question asked to granbpy
        Vars :
            - parser_answer
            - place_id_dict
            - parameter_status
            - map_status
    """
    map_status = data["map_status"]
    parameter_status = data["parameter_status"]
    # keyword isolation for question
    parse_answer = parser(question = data["question"])
    place_id_dict = get_place_id_list(address = " ".join(parse_answer))

    # creation and test public key api google map
    try:
        place_id = place_id_dict["candidates"][0]["place_id"]
    except IndexError:
        parameter_status["comprehension"] = False
        write_data(parameter_status)

    # creation of api google map coordinate address display setting
    # and wikipedia address history display setting
    map_status["answer"]["address"] = get_address(place_id = place_id)
    map_status["answer"]["history"] = get_history(
        search_history = " ".join(parse_answer)
    )
    map_status["data_map"]["address"] = map_status[
        "answer"]["address"]["result"]["formatted_address"]
    map_status["data_map"]["location"] = map_status[
        "answer"]["address"]["result"]["geometry"]["location"]
    # Display of the map according to the requested coordinates
    try:
        map_status["data_map"]
    except KeyError:
        parameter_status["quotas_api"] = True
        write_data(parameter_status)

    return map_status

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
    parameter_status = data["parameter_status"]
    map_status = data["map_status"]
    # display parameter map of requested coordinates
    display_map = get_map_static(map_status["data_map"])
    map_status["display_map"] = display_map
    # counting answer grandpy
    # ~ if parameter_status["nb_request"] == 10:
        # ~ parameter_status["quotas_api"] = True
        # ~ write_data(parameter_status)
    # response parameter to send
    return map_status

#========================
# save general parameter
#========================
def write_data(parameter):
    data = {
        "quotas_api": data_config.write_quotas(parameter["quotas_api"]),
        "civility": data_config.write_civility(parameter["civility"]),
        "decency": data_config.write_decency(parameter["decency"]),
        "comprehension": data_config.write_comprehension(parameter["comprehension"]),
        "nb_request": data_config.write_comprehension(parameter["nb_request"])
    }


#========================
# read general parameter
#========================
def read_data():
    data = {
        "quotas_api": data_config.read_quotas(),
        "civility": data_config.read_civility(),
        "decency": data_config.read_decency(),
        "comprehension": data_config.read_comprehension(),
        "nb_request": data_config.read_comprehension()
    }
    return data


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
    # Initialization of general parameters
    parameter_status = {
        "quotas_api": False,
        "civility": False,
        "decency": True,
        "comprehension": True,
        "nb_request": 0
    }
    # save general parameter
    write_data(parameter_status)
    # Initialization of geolocation parameters
    map_status = {
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
    # sending parameters
    data = {
        "question": question,
        "parameter_status": parameter_status,
        "map_status": map_status
    }
    # grandpy's reflection time to answer questions
    time_reflection = time.sleep(int(reflection))
    # politeness check
    wickedness(data)
    parameter_status = read_data()
    data["parameter_status"] = parameter_status
    # courtesy check
    if not parameter_status["civility"]:
        incivility(data)
        parameter_status = read_data()
    data["parameter_status"] = parameter_status
    # coordinate calculation
    data_status = map_coordinates(data)
    map_status = data_status
    data["parameter_status"] = read_data()
    data["map_status"] = map_status
    try:
        # control of the display of map coordinates
        coordonate_map = map_display(data)
    except TypeError:
        parameter_status["comprehension"] = False
        write_data(parameter_status)
    # state of the card coordinates
    map_status = coordonate_map
    # courtesy check to continue
    if parameter_status["civility"]:
        parameter_status["nb_request"] += 1
        write_data(parameter_status)
    # sending parameters
    data_send = {
        "parameter_status": read_data(),
        "map_status": map_status
    }
    return data_send

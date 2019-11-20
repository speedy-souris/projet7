#coding:utf-8
import time

from flask import Flask, render_template, request

from . import question_answer

app = Flask(__name__)

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/index/<reflection>/<question>")
def answer_gp(reflection, question):
    quotas_api = {"over_quotas": "False"}
    time_reflection = time.sleep(int(reflection))
    parse_answer = question_answer.parser(question = question)

    place_id_dict = question_answer.get_place_id_list(address = " ".join(parse_answer))
    try:
        place_id = place_id_dict["candidates"][0]["place_id"]
    except IndexError:
        quotas_api["over_quotas"] = "True"
        return {"quotas_api": quotas_api}

    answer = {
                "address": question_answer.get_address(place_id = place_id),
                "history": question_answer.get_history(search_history = " ".join(parse_answer))
    }

    try:
        data_map = {
                    "address": answer["address"]["result"]["formatted_address"],
                    "location": answer["address"]["result"]["geometry"]["location"]
        }
    except KeyError:
        quotas_api["over_quotas"] = "True"
        return {"quotas_api": quotas_api}

    display_map = question_answer.get_map_static(data_map)
    response = {"answer": answer, "display_map": display_map, "quotas_api": quotas_api}

    return response


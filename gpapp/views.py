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

    time_reflection = time.sleep(int(reflection))
    parse_answer = question_answer.parser(question = question)

    place_id_dict = question_answer.get_place_id_list(address = " ".join(parse_answer))
    place_id = place_id_dict["candidates"][0]["place_id"]

    answer = {
                "address": question_answer.get_address(place_id = place_id),
                "history": question_answer.get_history(search_history = " ".join(parse_answer))
    }

    data_map = {
                "address": answer["address"]["result"]["formatted_address"],
                "location": answer["address"]["result"]["geometry"]["location"]
    }

    display_map = {
                    "ref_map": question_answer.get_map_static(data_map)

    }

    return answer,display_map



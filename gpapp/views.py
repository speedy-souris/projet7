#coding:utf-8
#!/usr/bin/env python

import time

from flask import Flask, render_template
import chatdata
import main


app = Flask(__name__)

# main function for displaying answers
@app.route('/')
def index():
    """
        Initialization of the index.html page
        single home page
    """
    return render_template('index.html')

# initialization DataRedis
@app.route('/init')
def init():
    """
        Initialization of the dataRedis
    """
    _chatdata = chatdata.BehaviorDatabase()
    _chatdata.get_initial_database()
    return 'DataRedis initialized'

# Initialization of general parameters
@app.route('/index/<reflection>/<question>')
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
    time.sleep(int(reflection))
    # exchange between the user and grandpy
    data_discussion = main.main(question)
    # sending parameters
    data_send = {
        'grandpy_response': data_discussion[0].grandpy_response,
        'grandpy_code': data_discussion[0].grandpy_code,
        'map_status': {
            'address': data_discussion[1].get('address', ''),
            'map': data_discussion[1].get('map', ''),
            'history': data_discussion[1].get('history', '')
        }
    }
    return data_send


if __name__ == '__main__':
    pass

#coding:utf-8
import time

from flask import Flask, render_template, request

from . import question_answer

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/index/<reflection>')
def answer_gp(reflection):
    question = request.args.get('question')
    # ~ politeness = ['bonjour','salut','bonsoir']

    time_reflection = time.sleep(int(reflection))

    # ~ return render_template('index.html',
                                # ~ question = question, time_reflection = time_reflection)
    return 'blablabla'


# ~ if __name__ == "__main__":
    # ~ app.run()

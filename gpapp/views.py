#coding:utf-8
import time

from flask import Flask, render_template, request

from . import question_answer

app = Flask(__name__)

@app.route('/')
@app.route('/index/<reflection>')
def index(reflection):
    question = request.args.get('question')
    # ~ politeness = ['bonjour','salut','bonsoir']
    time_reflection = time.sleep(int(reflection))
    return render_template('index.html',
                                question = question, time_reflection = time_reflection)



# ~ if __name__ == "__main__":
    # ~ app.run()

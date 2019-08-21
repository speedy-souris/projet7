#coding:utf-8

from flask import Flask, render_template, request

from . import question_answer

app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/result/')
def result():
    question = request.args.get('question')
    # ~ politeness = ['bonjour','salut','bonsoir']

    return render_template('result.html',
                                question = question)

@app.route('/refletion/')
def reflexion():
    return render_template('refletion.html')

@app.route('/stress/')
def stress():
    return render_template('stress.html')

# ~ if __name__ == "__main__":
    # ~ app.run()

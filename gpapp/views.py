from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/result/')
def result():
    return render_template('result.html')

@app.route('/refletion/')
def reflexion():
    return render_template('refletion.html')

@app.route('/stress/')
def stress():
    return render_template('stress.html')

# ~ if __name__ == "__main__":
    # ~ app.run()

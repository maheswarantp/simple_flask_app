from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello There!!"


@app.route('/home')
def hello():
    return "Home api"

@app.route('/bye')
def bye():
    return "Bye api"
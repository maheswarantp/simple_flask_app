from flask import Flask
from flask import request, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    print(request.query_string)
    return "Hello There!!"

@app.route('/api', methods=['POST'])
def api():

    data = request.get_json()
    return data


@app.route('/home')
def home():
    return "Home api"

@app.route('/bye')
def bye():
    return "Bye api"
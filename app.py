from flask import Flask, Response, render_template
from flask import request, jsonify

app = Flask(__name__)
stringVal = ""
prevStringVal = ""


@app.route('/')
def hello():
    global stringVal
    print(request.args.get('energykey'))
    stringVal = request.args.get('energykey')
    return "Hello There!!"

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    return data

@app.route('/content', methods=['GET'])
def content():
    def inner():
        global stringVal, prevStringVal
        if stringVal != prevStringVal:
            prevStringVal = stringVal
            yield stringVal + '<br/>\n'
    return Response(inner(), mimetype='text/html')



@app.route('/home')
def home():
    return render_template('index.html.jinja')

@app.route('/bye')
def bye():
    return "Bye api"
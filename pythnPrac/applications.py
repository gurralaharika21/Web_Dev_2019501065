from flask import flask

app = Flask(__name__)

@app.route("/")
def index():
    return "hello,world!"

@app.route("/harika")
def index():
    return "hello,harika!"

@app.route("/raju")
def index():
    return "hello,raju!"

@app.route("/sri")
def index():
    return "hello,sri!"



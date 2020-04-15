from flask import flask

app = Flask(__name__)

@app.route("/")
def index():
    return "hello,world!"

@app.route("/<string:name>")  
def hello(name):
    name = name.capitalize()
    return f"<h1>Hello,{name}!</h1>"   
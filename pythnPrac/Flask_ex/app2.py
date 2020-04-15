from flask import Flask,render_template

app = Flase(__name__)

@app.route("/")
def index():
    return render_template("index.html")
from flask import Flask,render_template

app = Flase(__name__)

@app.route("/")
def index():
    headline = "Hello, world!!!"
    return render_template("index.html",headl ine = headline)

@app.route("/bye")
def bye():
    headline = "Goodbye!"    
    return render_template("index.html",headl ine = headline)
    
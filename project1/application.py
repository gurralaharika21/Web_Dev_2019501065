import os
from models import *
import datetime

from flask import Flask, session,redirect,request,render_template
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

import hashlib

# from model import Users,db


app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
Session(app)
db.init_app(app)


# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))
session = db()


# def main():
#     db.create_all()


# @app.route("/")
# def index():
#     return "Project 1: TODO"

@app.route("/", methods = ["POST","GET"])   
def register():
    # db.create_all()
    if request.method == "POST":
 
        # result = request.form
        name = request.form.get("name")
        
        email = request.form.get("email")
        password = request.form.get("psw")
        timestamp = datetime.datetime.now()
        print("name : ", name)
        print("email : ", email)
        print("password : ", hashlib.md5(password.encode()).hexdigest())
        print(timestamp)
 
        new_users = Users(name = name,email = email,password = hashlib.md5(password.encode()).hexdigest(),timestamp=timestamp)
        try:
            session.add(new_users)
            print(new_users)
            session.commit()
            # name = name
            print("commit completed")
            return render_template("result.html",name = name)
        except:
            
            return render_template("error.html")
    else:
        return render_template("register.html")            

       
        


@app.route("/admin", methods = ["GET"])
def users_info():
    # data = Users.query.all()
    data = db.query(Users)
    return render_template("users.html",data = data)        

       
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = "Users"
    # id = db.Column(db.Serial,primary_key = True,nullable = False)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, primary_key=True)
    password = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)


    def __init__(self,name,email,password,timestamp):
        self.name = name
        self.email = email
        self.password = password
        self.timestamp = timestamp

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()           


class Myuser(db.Model): 
    __tablename__ = 'myUser'   
    id = db.Column(db.Integer, primary_key = True)   
    userName = db.Column(db.String(30))
    userEmail = db.Column(db.String(32), unique = True)       
    password = db.Column(db.String(64))


class TimeCheck(db.Model):
    __tablename__ = 'timeCheck'
    id = db.Column(db.Integer , primary_key = True)
    myuserId = db.Column(db.Integer , db.ForeignKey('myUser.id'), nullable=False)
    timeType = db.Column(db.String(7))
    whatTime = db.Column(db.String(30))
    startEnd = db.Column(db.String(7))
    timeStamp = db.Column(db.DateTime, server_default=db.func.now())

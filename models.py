from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()           

class Myuser(db.Model): 
    __tablename__ = 'myUser'   
    id = db.Column(db.Integer, primary_key = True)   
    userName = db.Column(db.String(30))
    userEmail = db.Column(db.String(32))       
    password = db.Column(db.String(64))



class TimeCheck(db.Model):
    __tablename__ = 'timeCheck'
    id = db.Column(db.Integer , primary_key = True)
    startTime = db.Column(db.String(18))
    endTime = db.Column(db.String(18))
    plusMinus = db.Column(db.String(2))
    whatTime = db.Column(db.String(30))
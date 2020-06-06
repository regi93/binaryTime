from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Email
# from app import db
from models import db , MyUser

class RegisterForm(FlaskForm):
    userEmail = StringField('userEmail', validators=[DataRequired() , Email()])
    #Email Validator 추가할것
    userName = StringField('userName', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), EqualTo('rePassword')]) 
    rePassword = PasswordField('rePassword', validators=[DataRequired()])


class LoginForm(FlaskForm):
    class UserPassword(object):
        def __init__(self, message=None):
            self.message = message
        def __call__(self,form,field):
            userEmail = form['userEmail'].data
            password = field.data
            # myuser = Myuser.query.filter_by(userEmail = userEmail).first()
            if type(MyUser.login(userEmail)) == str:
                raise ValueError('Wrong Email')
                
            elif MyUser.login(userEmail)[0] != password:
                print("Wrong Password")
                raise ValueError('Wrong password')
            
    userEmail = StringField('userid', validators=[DataRequired(), Email() ])
    password = PasswordField('password', validators=[DataRequired(), UserPassword()]) 

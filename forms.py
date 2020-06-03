from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo
from models import Myuser

class RegisterForm(FlaskForm):
    userEmail = StringField('userEmail', validators=[DataRequired()])
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
            myuser = Myuser.query.filter_by(userEmail = userEmail).first()
            if myuser.password != password:
                raise ValueError('Wrong password')
    userEmail = StringField('userid', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), UserPassword()]) 

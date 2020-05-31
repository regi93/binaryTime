from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo

class RegisterForm(FlaskForm):
    userEmail = StringField('userEmail', validators=[DataRequired()])
    userName = StringField('userName', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), EqualTo('rePassword')]) 
    rePassword = PasswordField('rePassword', validators=[DataRequired()])
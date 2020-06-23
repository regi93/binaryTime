import os
from flask import Flask , request , redirect , render_template, session, jsonify
from flask_wtf.csrf import CSRFProtect 
from forms import RegisterForm , LoginForm
from models import db , MyUser
from api_v1 import api as api_v1

app = Flask(__name__)
app.register_blueprint(api_v1 , url_prefix='/api/v1')

@app.route('/time')
def time():
    return render_template('time.html')
    
@app.route('/user/<w>',methods=["POST","GET"])
def login(w):
    if w == 'login':
        form = LoginForm()
        mode = 'login'
        if form.validate_on_submit(): 
            session['userEmail'] = form.data.get('userEmail')    
            userEmail = session['userEmail']
            return redirect ('/')
    elif w == 'register':
        form = RegisterForm()
        mode = 'register'
        if form.validate_on_submit():     
            userEmail = form.data.get('userEmail')
            userName = form.data.get('userName')
            password = form.data.get('password')
            userInfo = {
                'userEmail': userEmail ,
                'userName': userName ,
                'password' : password
            }
            if MyUser.login(userEmail) == 'Wrong Email':
                db.userInfo.insert_one(userInfo)
                return redirect ('/user/login')
            else : 
                return redirect('/user/register')
    return render_template('login.html',form=form , mode=mode)

@app.route('/')
def hello():
    userEmail = session.get('userEmail', None)
    if userEmail:
        userName = MyUser.login(userEmail)[1]
        return render_template('index.html',userName = userName)
    return "do login"

@app.route('/chart')
def chart():
    return render_template('chart.html')

if __name__ == "__main__":
    app.config['SECRET_KEY'] = 'this is SEcret Key'
    csrf = CSRFProtect() 
    csrf.init_app(app)
    csrf.exempt(api_v1)

    app.run(host='0.0.0.0', port=5000, debug=True)
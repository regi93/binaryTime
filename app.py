import os
from flask import Flask , request , redirect , render_template, session, jsonify
from flask_wtf.csrf import CSRFProtect 
from forms import RegisterForm , LoginForm
from models import db , MyUser
from api_v1 import api as api_v1

# from models import Myuser ,db , TimeCheck

# import datetime
# date , time = str(datetime.datetime.now()).split()
# year ,month, day = date.split("-")
# hour , minute , second = time[:8].split(":") 
# print(year, month, day)
# data = "%s-%s-%s"%(year,month,second)

app = Flask(__name__)
app.register_blueprint(api_v1 , url_prefix='/api/v1')



@app.route('/time')
def time():
    return render_template('time.html')

@app.route('/register', methods=['GET','POST'])
def register():   
    form = RegisterForm()
    if form.validate_on_submit():     
        userEmail = form.data.get('userEmail')
        userName = form.data.get('userName')
        password = form.data.get('password')
        userInfo = {
            'userEmail': userEmail ,
            'userName': userName ,
            'password' : password
        }
        db.userInfo.insert_one(userInfo)
        # db.session.add(myuser)  
        # db.session.commit()  
        return "register Success"
            
    return render_template('register.html', form=form)

@app.route('/login',methods=["POST","GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit(): 
        session['userEmail'] = form.data.get('userEmail')    
        userEmail = session['userEmail']
        return redirect ('/')
    return render_template('login.html', form=form)

@app.route('/')
def hello():
    
    if session['userEmail']:
        userEmail = session['userEmail']
        userName = MyUser.login(userEmail)[1]
    # return render_template('index.html', userName=userName)
        return render_template('index.html',userName = userName)
    return "do login"


if __name__ == "__main__":
    # basedir = os.path.abspath(os.path.dirname(__file__)) 
    # dbfile = os.path.join(basedir, 'db.sqlite')
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile   
    # app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True 
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
    app.config['SECRET_KEY'] = 'this is SEcret Key'
    csrf = CSRFProtect() 
    csrf.init_app(app)
    # db.init_app(app)
    # db.app = app
    # db.create_all()  
    app.run(host='127.0.0.1', port=5000, debug=True) 


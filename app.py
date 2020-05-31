import os
from flask import Flask , request , redirect , render_template
from models import Myuser ,db , TimeCheck
from flask_wtf.csrf import CSRFProtect
from forms import RegisterForm
import datetime


app = Flask(__name__)


@app.route('/register', methods=['GET','POST'])
def register():   
    form = RegisterForm()
    if form.validate_on_submit():     
        myuser = Myuser() 
        myuser.userEmail = form.data.get('userEmail')
        myuser.userName = form.data.get('userName')
        myuser.password = form.data.get('password')
        db.session.add(myuser)  
        db.session.commit()  
        return "가입 완료"
            
    return render_template('register.html', form=form)

@app.route('/')
def hello():
    return render_template('index.html' , date = printDate)   

@app.route('/time')
def time():
    
    return render_template('time.html')

if __name__ == "__main__":
    basedir = os.path.abspath(os.path.dirname(__file__)) 
    dbfile = os.path.join(basedir, 'db.sqlite')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile   
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
    app.config['SECRET_KEY'] = 'this is SEcret Key'
    csrf = CSRFProtect()
    csrf.init_app(app)
    db.init_app(app)
    db.app = app
    db.create_all()  
    app.run(host='127.0.0.1', port=5000, debug=True) 


now = datetime.datetime.now()
print(now)
from app import Blueprint , render_template , request , flash , redirect , url_for , jsonify
from .models import User
from werkzeug.security import generate_password_hash , check_password_hash
from . import db
from flask_login import login_user , login_required , logout_user , current_user
#from stackframes import dump
auth = Blueprint('auth' , __name__ )



@auth.route('/login' , methods=['GET' , 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

    #Checking if a user with that email exists(searching specific entry in our database)
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password , password):
                flash('Logged in succefully' , category ='success')
                login_user(user , remember=True)
                return redirect(url_for('views.home'))

            else: 
                flash('Incorrect password, please try again' , category ='error')
        else:
            flash('Email does not exist.' , category = 'error')
   # data = request.form
   # print(data)
    return render_template("login.html" , text="Testing" , user="Raf")



@auth.route('/logout')
#Cannot access this page unless user is logged in
@login_required
def logout():
    #Using logout_user we redirect to auth login
    logout_user
    return redirect(url_for('auth.login'))

@auth.route('/register' , methods=['GET' , 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('This user already exist' , category = 'error')

        if len(email) <= 4:
            flash('Email must be greater than 4 characters.' , category='error')
        elif len(firstname) < 2 :
            flash('First name must be greater than 2 characters.' , category='error')
        elif password1 != password2:
            flash('Passwords dont match.' , category='error' )

        elif len(password1) < 7 :
            flash('Password must be at least 7 characters.' , category='error')
        else:
            new_user = User(email = email , firstname = firstname ,  password= generate_password_hash(password1 , method = 'SHA256'))
          #  dump(new_user)
            db.session.add(new_user)
            db.session.commit()
            login_user(user , remember=True)
            redirect(url_for('views.home'))
            flash('Account created!' , category= 'success')

    return render_template("register.html")



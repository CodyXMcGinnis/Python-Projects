from flask import render_template, redirect,request,session, flash
from flask_app import app
from datetime import datetime
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/success')
def success():
    if 'user_id' not in session:
        return redirect('/logout')
    data={
        'id': session['user_id']
    }
    return render_template("success.html",user=User.get_by_id(data))

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/create/user', methods=['POST'])
def create_user():
    if not User.validate_user(request.form):
        return redirect('/')

    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "username": request.form['username'],
        "password": bcrypt.generate_password_hash(request.form['password']),
        "birthday": datetime.strptime(request.form['birthday'], '%Y-%m-%d'),
        "pro_lang": request.form['pro_lang'],
        "cat_dog": request.form['cat_dog'],
        "seasons": request.form['seasons']
    }
    
    id = User.save(data)
    session['user_id'] = id
    return redirect('/success')

@app.route('/login/user', methods=['POST'])
def login_user():
    user = User.get_by_email(request.form)
    
    if not user:
        flash("Invalid Email","login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password", "login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/success')
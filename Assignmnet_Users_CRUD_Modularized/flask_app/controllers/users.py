from flask import render_template,redirect,request,session
from flask_app import app
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template("users.html",users=User.get_all())

@app.route('/users/new')
def new():
    return render_template("create_user.html")

@app.route('/users/create',methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')

@app.route('/users/edit/<int:id>')
def edit(id):
    data={
        "id":id
    }
    return render_template("edit_user.html", user=User.get_one(data))

@app.route('/users/update',methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/users/delete/<int:id>')
def delete(id):
    data={
        "id":id
    }
    User.delete(data)
    return redirect('/users')

@app.route('/users/show/<int:id>')
def show(id):
    data={
        "id":id
    }
    return render_template("user_details.html", user=User.get_one(data))
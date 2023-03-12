from flask import render_template,redirect,request,url_for
from flask_app import app
from flask_app.models import dojo, ninja

@app.route('/ninjas')
def new():
    return render_template("create_ninja.html", dojos=dojo.Dojo.get_all())

@app.route('/create/ninja',methods=['POST'])
def create_ninja():
    id = request.form.get('dojo_id')
    ninja.Ninja.save(request.form)
    return redirect(url_for('show_dojo', id=id))

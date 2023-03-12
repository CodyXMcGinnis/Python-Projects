from flask import Flask, render_template, redirect, session,request
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes
# our index route will handle rendering our form
@app.route('/')
def index():       
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    session['fav_language'] = request.form['fav_language']
    session['vehicle'] = request.form.getlist('vehicle')
    session['cars'] = request.form['cars']
    session['comments'] = request.form['comments']
    
    return redirect('/result')

@app.route('/result')
def result():       
    return render_template('results.html', name_on_template=session['name'],
                            email_on_template=session['email'],
                            fav_lang_on_template=session['fav_language'],
                            vehicle_on_template=session['vehicle'],
                            cars_on_template=session['cars'],
                            comments_on_template=session['comments'])

if __name__ == "__main__":
    app.run(debug=True)
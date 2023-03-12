from flask import Flask, render_template, redirect, session,request
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes
# our index route will handle rendering our form
@app.route('/')
def index():
    if 'counter' not in session:
        session['counter']=0
    else:
        session['counter'] += 1
    if 'visits' not in session:
        session['visits']=0
    else:    
        session['visits'] += 1        
    return render_template("index.html")

@app.route('/destroy_session')
def clear_session():
    session.clear()
    return redirect('/')	 
    
# adding this method
@app.route('/reset')
def rest():
    session.pop('counter')
    return redirect('/')

@app.route('/manual', methods=['POST'])
def manual():
    count =int(request.form['count']) - 1
    session['counter'] += count
    return redirect('/')

@app.route('/addtwo')
def addtwo():
    session['counter'] += 1
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
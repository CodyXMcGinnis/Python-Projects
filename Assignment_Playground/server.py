from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template("index.html", times=0, color="blue")

@app.route('/play')
def level_one():
    return render_template("index.html", times=3, color="blue")

@app.route('/play/<int:times>')
def level_two(times):
    return render_template("index.html", times=times, color="blue")

@app.route('/play/<int:times>/<string:color>')
def level_three(times, color):
    return render_template("index.html", times=times, color=color)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
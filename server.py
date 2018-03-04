from flask import Flask, render_template
from flask_socketio import SocketIO, send, join_room, leave_room

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("Home.html")

@app.route('/about')
def about():
    return render_template("About.html")

@app.route('/contact', methods = ['POST'])
def contact():

    if request.method == 'POST':

    contact = request.form['Name']
    
    return "Name: " + contact

if __name__ == '__main__':
    app.run(debug = True)

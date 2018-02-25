from flask import Flask, render_template
from flask_socketio import SocketIO, send, join_room, leave_room

app = Flask(__name__)
app.config['SECRET KEY'] = '123'
app.debug = True
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template("generatecode.html")

@app.route('/test')
def foo():
    return render_template("test.html")

if __name__ == "__main__":
    socketio.run(app)

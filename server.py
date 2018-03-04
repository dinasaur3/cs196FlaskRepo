from flask import Flask, render_template
from flask import flask_wtf
from wtforms import StringField, SubmitField

from flask_socketio import SocketIO, send, join_room, leave_room

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("Home.html")

@app.route('/about')
def about():
    return render_template("About.html")

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    form = ContactForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        #session sets the borders of a conversation with the database.            
        db_session.add(user)
        flash('Thank you')
        return redirect(url_for('login'))
    return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.run(debug = True)

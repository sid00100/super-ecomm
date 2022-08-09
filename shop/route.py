from flask import render_template
from shop import app
from shop.form import Sign_up

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route("/signup")
def signup():
    form = Sign_up()
    return render_template("signup.html", form = form)
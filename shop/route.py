from flask import render_template, request, flash

from shop import app

from shop.form import Sign_up

from firebase_admin import auth


@app.route('/')
@app.route('/home')
def home_page():

    return render_template('home.html')


@app.route("/signup", methods=["GET", "POST"])
def signup():

    form = Sign_up()

    if form.validate_on_submit():
        username = form.username.data

        email = form.email.data

        password = form.password.data

        try:
            user = auth.create_user(email=email, password=password)
        except:
            auth.EmailAlreadyExistsError
            print("user already exist")

    return render_template("signup.html", form=form)

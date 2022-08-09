from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, EqualTo

class Sign_up(FlaskForm):
    username = StringField(label="username" ,validators=[DataRequired()])
    email = EmailField()
    password = PasswordField(validators=[DataRequired()])
    password_confirm = PasswordField(validators=[DataRequired(), EqualTo("password") ])
    submit = SubmitField()

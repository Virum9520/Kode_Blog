from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                        validators=[DataRequired(), Length(2, 10)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField(label='Password',
                        validators=[DataRequired()])
    confirm_password = PasswordField(label='Confirm Password',
                        validators=[DataRequired(), EqualTo("password")])
    submit_button = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField(label='Password',
                        validators=[DataRequired()])
    remember_cookie = BooleanField('Remember me')
    submit_button = SubmitField('Login')

print("")

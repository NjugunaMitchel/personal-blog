from flask_wtf import Flaksform
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtfforms.validators import DataRequired, Length, Email, EqualTo


class Signupform(Flaksform):
    username = StringField('username',validators=[DataRequired(),Length(min=3, max=0)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired()])
    confirm_password = PasswordField('confirm_password',validators=[DataRequired(),EqualTo('password')])
    submit  = SubmitField('Sign Up')



class Signupform(Flaksform):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit  = SubmitField('Login')
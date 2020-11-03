from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from ..models import Users

class Signupform(FlaskForm):
    username = StringField('username',validators=[DataRequired(),Length(min=3, max=20)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired()])
    confirm_password = PasswordField('confirm_password',validators=[DataRequired(),EqualTo('password')])
    submit  = SubmitField('Sign Up')


    def validate_email(self,data_field):
         if Users.query.filter_by(email =data_field.data).first():
             raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
         if Users.query.filter_by(username = data_field.data).first():
             raise ValidationError('That username is taken')


class Loginform(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit  = SubmitField('Login')
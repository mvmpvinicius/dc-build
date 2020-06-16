from flask_wtf import FlaskForm
from wtforms import (
    HiddenField, PasswordField, StringField, SubmitField)
from wtforms.validators import DataRequired, Email, EqualTo, Length


class ExampleForm(FlaskForm):
    id = HiddenField()
    name = StringField('name', validators=[DataRequired()])


class UserForm(FlaskForm):
    id = HiddenField()
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Length(
        min=6), Email(message='Not a valid email')])
    password = PasswordField('password', validators=[
                             DataRequired(), Length(min=6)])
    confirm = PasswordField('c_password', validators=[
                            EqualTo(
                                'password', message='Different passwords')])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField(
        'email', validators=[
            DataRequired(), Email(message='Not a valid email')])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Log In')

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField, SelectMultipleField, TextAreaField, IntegerField
from wtforms.validators import DataRequired


class SignupForm(FlaskForm):
    email = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    name = StringField('Name')
    lastname = StringField('Name')
    telephone = IntegerField('telephone')
    profession = StringField('Name')
    submit = SubmitField('signup')
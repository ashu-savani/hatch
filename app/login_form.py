from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, DateField
from wtforms.validators import DataRequired
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User
from datetime import date

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    phone_number = IntegerField("PhoneNumber", validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

class SellingForm(FlaskForm):
    quantity = IntegerField("Quantity", validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired()])
    produce = StringField("Produce", validators=[DataRequired()])
    date_start = DateField("Start Date", validators=[DataRequired()], default=date.today())
    date_end = DateField("End Date", validators=[DataRequired()])
    submit = SubmitField("Add")

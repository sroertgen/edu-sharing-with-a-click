from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, IPAddress


class RegistrationForm(FlaskForm):
    institution = StringField('Institution', validators=[
                              DataRequired(), Length(min=5, max=100)])
    firstname = StringField('Firstname',
                            validators=[DataRequired(), Length(min=2, max=20)])
    lastname = StringField('Lastname',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    street = StringField('Street',
                         validators=[DataRequired(), Length(min=2, max=20)])
    housenumber = StringField('Housenumber',
                              validators=[DataRequired(), Length(min=1, max=20)])
    location = StringField('Location',
                           validators=[DataRequired(), Length(min=2, max=20)])
    zip = StringField('Zip',
                      validators=[DataRequired(), Length(min=2, max=20)])

    user_number_choices = [('1', 'Moodle'),
                           ('2', 'Wordpress'),
                           ('3', 'edu-sahring')]

    usernumber = SelectField(
        'User_number', choices=user_number_choices, validators=[DataRequired()])

    ip1 = StringField('IP1', validators=[
                      DataRequired(), IPAddress()])

    ip2 = StringField('IP2', validators=[IPAddress()])

    submit = SubmitField('Absenden')

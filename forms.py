from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, IPAddress


class RegistrationForm(FlaskForm):
    institution = StringField('Institution', validators=[DataRequired(), Length(min=4, max=100)])

    firstname = StringField('Vorname', validators=[DataRequired(), Length(min=2, max=20)])

    lastname = StringField('Nachname', validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField('Email', validators=[DataRequired(), Email()])

    street = StringField('Straße', validators=[DataRequired(), Length(min=2, max=20)])

    housenumber = StringField('Hausnummer', validators=[DataRequired(), Length(min=1, max=20)])

    location = StringField('Ort', validators=[DataRequired(), Length(min=2, max=20)])
    zip = StringField('PLZ', validators=[DataRequired(), Length(min=2, max=20)])

    instance_choices = [('1', 'Moodle'),
                        ('2', 'Wordpress'),
                        ('3', 'edu-sahring')]

    instance = SelectField(
        'Welche Art von Instanz?', choices=instance_choices, validators=[DataRequired()])

    ip1 = StringField('IP1', validators=[DataRequired(), IPAddress()])

    # ip2 = StringField('IP2 (nur bei edu-sharing nötig, sont leer lassen)', validators=[IPAddress()])

    uname = StringField("Username auf Server", validators=[DataRequired()])

    upasswd = StringField("Passwort des Nutzers auf Server")

    submit = SubmitField('Absenden')

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired, Length, Email, IPAddress


class RegistrationForm(FlaskForm):
    institution = StringField('Institution', render_kw={"placeholder": "Institution"})
    # institution = StringField('Institution', validators=[DataRequired(), Length(min=4, max=100)], render_kw={"placeholder": "Institution"})

    firstname = StringField('Vorname', render_kw={"placeholder": "Vorname"})

    lastname = StringField('Nachname', render_kw={"placeholder": "Nachname"})

    email = StringField('Email', render_kw={"placeholder": "Email"})

    street = StringField('Straße', render_kw={"placeholder": "Straße"})

    housenumber = StringField('Hausnummer')

    location = StringField('Ort', render_kw={"placeholder": "Ort"})

    zip = StringField('PLZ', render_kw={"placeholder": "PLZ"})

    instance_choices = [('0', 'Bitte auswählen...'),
                        ('moodle', 'Moodle'),
                        ('wordpress', 'Wordpress'),
                        ('edusharing', 'edu-sharing (optional mit Moodle)')]

    instance = SelectField(
        'Welche Art von Instanz?', choices=instance_choices, validators=[DataRequired()])

    ip1 = StringField('IP1', validators=[DataRequired(), IPAddress()], render_kw={"placeholder": "192.168.178.1"})

    uname1 = StringField("Username auf Server (IP1)", validators=[DataRequired()])

    upasswd1 = StringField("Passwort des Nutzers auf Server (IP1)")

    domain1 = StringField("Domain des Servers (ohne http:// oder https:// )")

    ip2 = StringField('IP2 (nur bei edu-sharing nötig, sont leer lassen)',
                      render_kw={"placeholder": "192.168.178.1"})

    uname2 = StringField("Username auf Server (IP2)")

    upasswd2 = StringField("Passwort des Nutzers auf Server (IP2)")

    moodle_registration = BooleanField("Soll zusätzlich eine Moodle-Instanz eingerichtet und mit dem Edu-Sharing Repositorium verbunden werden?")

    moodle_ip = StringField('IP der Moodle-Instanz)',
                        render_kw={"placeholder": "192.168.178.2"})

    moodle_uname = StringField("Username auf Moodle-Instanz")

    moodle_pw = StringField("Passwort des Users auf Moodle-Instanz")

    moodle_domain = StringField(
        "Domain des Moodle Servers (ohne http:// oder https:// )")

    submit = SubmitField('Absenden')

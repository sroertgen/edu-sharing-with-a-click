from flask import Flask, render_template, url_for, flash, redirect, request, Response, session
from forms import RegistrationForm
from edit_yml import edit_yml
from run_ansible import run_ansible
import subprocess
import time

yml_entries = []
instance_choice = []
choice = []
moodle_registration = 0

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SECRET_KEY'] = '5adb4994226fcac5c135af59f4654483'

# Index der Web-App
@app.route("/", methods=["GET", "POST"])
def index():

    return render_template("index.html")

# Registrierung
@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        flash(f"Auf geht's!", 'success')
        yml_entries = {
            "ip1": form.ip1.data,
            "domain1": form.domain1.data,
            "email": form.email.data,
            "uname1": form.uname1.data,
            "upasswd1": form.upasswd1.data,
            "ip2": form.ip2.data,
            "uname2": form.uname2.data,
            "upasswd2": form.upasswd2.data,
            "moodle_ip": form.moodle_ip.data,
            "moodle_uname": form.moodle_uname.data,
            "moodle_pw": form.moodle_pw.data,
            "moodle_domain": form.moodle_domain.data
        }

        if form.moodle_registration.data == 1:
            moodle_registration = 1

            print(f"User chose {moodle_registration}")
        else:
            moodle_registration = 0

        session['moodle_registration'] = moodle_registration
        moodle_registration = session.get('moodle_registration', None)

        session['instance_choice'] = form.instance.data
        instance_choice = session.get('instance_choice', None)

        edit_yml(yml_entries, instance_choice, moodle_registration)
        return redirect(url_for("registration_data"))

    return render_template("register.html", form=form)


# Soll die Daten noch einmal in übersichtlicher Art und Weise darstellen
# noch nicht implementiert
@app.route("/registration-data", methods=["GET", "POST"])
def registration_data():
    instance_choice = session.get('instance_choice', None)

    print(f"User choosed: {instance_choice}")

    session['instance_choice'] = instance_choice

    return render_template("registration-data.html")


# führt das Skript run_ansible aus und zeigt den Output im Browser an
@app.route("/make-instance", methods=["GET", "POST"])
def make_instance():
    instance_choice = session.get('instance_choice', None)
    moodle_registration = session.get('moodle_registration', None)

    return Response(run_ansible(instance_choice, moodle_registration), mimetype='text/html')


# alt und kann vermutlich gelöscht werden
# @app.route("/test", methods=["GET", "POST"])
# def test():

#     def inner():
#         proc = subprocess.Popen(["ansible-playbook", "ansible-files/wp-playbook.yml", "-i", "ansible-files/inventory.txt"], stdout=subprocess.PIPE, universal_newlines=True)
#         print("I'm running")
#         for line in iter(proc.stdout.readline, ''):
#             time.sleep(0.2)
#             yield line.rstrip() + '<br/>\n'

#     return Response(inner(), mimetype='text/html')  # text/html is required for most browsers to show output


if __name__ == "__main__":
    app.run(debug=True)

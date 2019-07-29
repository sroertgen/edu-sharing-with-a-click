from flask import Flask, render_template, url_for, flash, redirect, request, Response, session
from forms import RegistrationForm
from edit_yml import edit_yml
from run_ansible import run_ansible
import subprocess
import time

yml_entries = []
instance_choice = []
choice = []

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SECRET_KEY'] = '5adb4994226fcac5c135af59f4654483'


@app.route("/", methods=["GET", "POST"])
def index():

    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        flash(f"Auf geht's!", 'success')
        yml_entries = {
            "ip1": form.ip1.data,
            "email": form.email.data,
            "uname": form.uname.data,
            "upasswd": form.upasswd.data
        }
        session['instance_choice'] = form.instance.data
        print(instance_choice)
        edit_yml(yml_entries)
        return redirect(url_for("registration_data"))

    return render_template("register.html", form=form)


@app.route("/registration-data", methods=["GET", "POST"])
def registration_data():
    instance_choice = session.get('instance_choice', None)

    print(f"User choosed: {instance_choice}")

    session['instance_choice'] = instance_choice

    return render_template("registration-data.html")


@app.route("/make-instance", methods=["GET", "POST"])
def make_instance():
    instance_choice = session.get('instance_choice', None)

    return Response(run_ansible(instance_choice), mimetype='text/html')


@app.route("/test", methods=["GET", "POST"])
def test():

    def inner():
        proc = subprocess.Popen(["ansible-playbook", "ansible-files/wp-playbook.yml", "-i", "ansible-files/inventory.txt"], stdout=subprocess.PIPE, universal_newlines=True)
        print("I'm running")
        for line in iter(proc.stdout.readline, ''):
            time.sleep(0.2)
            yield line.rstrip() + '<br/>\n'

    return Response(inner(), mimetype='text/html')  # text/html is required for most browsers to show th$


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm
from edit_yml import edit_yml
from run_ansible import run_ansible

yml_entries = []

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SECRET_KEY'] = '5adb4994226fcac5c135af59f4654483'


@app.route("/", methods=["GET", "POST"])
def index():
    form = RegistrationForm()

    if form.validate_on_submit():
        flash(f"Will start to create your account for now!", 'success')
        yml_entries = [
            form.ip1.data,
            form.email.data,
        ]
        edit_yml(yml_entries)

    return render_template("index.html", form=form)


@app.route("/moodle", methods=["GET", "POST"])
def moodle():
    form = RegistrationForm()

    instance = "moodle"
    run_ansible(instance)

    return render_template("moodle.html", form=form)


@app.route("/wordpress", methods=["GET", "POST"])
def wordpress():
    form = RegistrationForm()
    return render_template("wordpress.html", form=form)


@app.route("/edu-sharing", methods=["GET", "POST"])
def edu_sharing():
    form = RegistrationForm()
    return render_template("edu-sharing.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)

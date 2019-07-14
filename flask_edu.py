from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm


app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SECRET_KEY'] = '5adb4994226fcac5c135af59f4654483'


@app.route("/", methods=["GET", "POST"])
def index():
    form = RegistrationForm()

    if form.validate_on_submit():
        flash(f"Will start to create your account for now!", 'success')

    print(form.ip2.raw_data)
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)

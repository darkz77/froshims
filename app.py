from flask import Flask, render_template, request


app = Flask(__name__)

REGISTRANTS = {}

SPORTS = ["Basketball", "Soccer", "Ultimate Frisbee"]


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", sports = SPORTS)


@app.route("/register", methods=["POST"])
def register():
    if not request.form.get("name"):
        return "failure"
    for sport in request.form.getlist("sport"):
        if sport not in SPORTS:
            return "failure"
    return "success"

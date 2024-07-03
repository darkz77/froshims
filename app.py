from flask import Flask, render_template, request, session, redirect
from flask_session import Session


app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# SPORTS = ["Basketball", "Soccer", "Ultimate Frisbee"]


@app.route("/")
def index():
    return render_template("index.html", name=session.get("name"))


# @app.route("/register", methods=["POST"])
# def register():
#     if not request.form.get("name"):
#         return "failure"
#     for sport in request.form.getlist("sport"):
#         if sport not in SPORTS:
#             return "failure"
#     return "success"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["name"] = request.form.get("name")
        return redirect("/")
    return render_template("login.html")


@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.clear()
    return redirect("/")


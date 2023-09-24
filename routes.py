from app import app
from flask import redirect, render_template, request
import registerpy 


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register")
def new_registeration():
    return render_template("register.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if registerpy.register(username, password):
            return redirect("/")
        else:
            return render_template("register.html")
    
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if registerpy.login(username, password):
            count = registerpy.count_plants()
            return render_template("user.html", count=count)
        else:
            return render_template("index.html")

@app.route("/logout")
def logout():
    registerpy.logout()
    return redirect("/")

@app.route("/new_plant", methods=["GET", "POST"])
def new_plant():
    if request.method == "GET":
        return render_template("plant.html")

@app.route("/add_plant", methods=["GET", "POST"])
def add_plant():
    if request.method == "GET":
        return render_template("plant.html")
    if request.method == "POST":
        name = request.form["name"]
        latinname = request.form["latinname"]
        light = request.form["light"]
        water = request.form["water"]
        other = request.form["other"]
        if registerpy.add_plant(name, latinname, light, water, other):
            count = registerpy.count_plants()
            return render_template("user.html", count=count)
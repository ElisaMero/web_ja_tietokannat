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
            registerpy.create_emojis_table()
            count = registerpy.count_plants()
            name = registerpy.show_user()
            plant_name = registerpy.plant_headings()
            emoji = registerpy.choose_emoji()
            return render_template("user.html", count=count, name=name, plant_name=plant_name, emoji=emoji)
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
            name = registerpy.show_user()
            plant_name = registerpy.plant_headings()
            emoji = registerpy.choose_emoji()
            return render_template("user.html", count=count, name=name, plant_name=plant_name, emoji=emoji)


@app.route("/headings", methods=["GET", "POST"])
def heading_routes():
    name = request.args.get("name")
    theplantname = request.args.get("theplantname")
    comment = registerpy.get_comments(theplantname)
    info = registerpy.plant_info(theplantname)
    count = registerpy.count_plants()
    name = registerpy.show_user()
    plant_name = registerpy.plant_headings()
    emoji = registerpy.choose_emoji()
    return render_template("user.html", info=info, count=count, name=name, plant_name=plant_name, comment=comment, emoji=emoji)


@app.route("/notes", methods=["GET", "POST"])
def add_notes():
    comment1 = request.form["plantname"]
    theplantname = request.args.get("theplantname")
    registerpy.add_notes(comment1, theplantname)
    return redirect(f"/headings?theplantname={theplantname}")


@app.route("/search", methods=["GET"])
def result():
    input = request.args.get("word")
    plant_name = registerpy.search_generator(input)
    count = registerpy.count_plants()
    name = registerpy.show_user()
    emoji = registerpy.choose_emoji()
    return render_template("user.html", count=count, name=name, plant_name=plant_name, emoji=emoji)

from app import app
import secrets
from flask import redirect, render_template, request, session, flash
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
        return render_template("register.html", same_name=True)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if registerpy.login(username, password):
            session["username"] = username
            session["csrf_token"] = secrets.token_hex(16)
            registerpy.create_emojis_table()
            count = registerpy.count_plants()
            name = registerpy.show_user()
            plant_name = registerpy.plant_headings()
            emoji = registerpy.choose_emoji()
            return render_template("user.html", count=count, name=name, plant_name=plant_name, emoji=emoji)
        else:
            return render_template("error.html")


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
        if session["csrf_token"] != request.form.get("csrf_token"):
            return render_template("error.html")
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
        return render_template("plant.html", same_name=True)


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
    if session["csrf_token"] != request.form.get("csrf_token"):
        return render_template("error.html")
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


@app.route("/delete_plant")
def delete_plant():
    name = request.args.get("name")
    print(name)
    registerpy.delete_plant(name)
    count = registerpy.count_plants()
    name = registerpy.show_user()
    emoji = registerpy.choose_emoji()
    plant_name = registerpy.plant_headings()
    return render_template("user.html", count=count, name=name, emoji=emoji,
                           plant_name=plant_name)


@app.route("/direction")
def open_directions():
    registerpy.create_direction_table()
    return render_template("directions.html")


@app.route("/pothos")
def show_pothos():
    info = registerpy.show_pothos()
    return render_template("directions.html", info=info)


@app.route("/snake")
def show_snake():
    info = registerpy.show_snake()
    return render_template("directions.html", info=info)


@app.route("/back")
def go_back():
    count = registerpy.count_plants()
    name = registerpy.show_user()
    emoji = registerpy.choose_emoji()
    plant_name = registerpy.plant_headings()
    return render_template("user.html", count=count, name=name, emoji=emoji,
                           plant_name=plant_name)

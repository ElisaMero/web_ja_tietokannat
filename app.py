from flask import Flask
from flask import redirect, render_template, request, session
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register.html", methods=["POST"])
def register():
    username = request.form["username"]
    password = request.form["password"]
#    hash_value = generate_password_hash(password)
 #   sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
  #  db.session.execute(sql, {"username":username, "password":hash_value})
   # db.session.commit()



@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    # check username and password here!
    session["username"] = username
    return redirect("/")

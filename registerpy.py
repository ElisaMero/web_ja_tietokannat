
from database import db
from flask import session
from sqlalchemy.sql import text
from werkzeug.security import check_password_hash, generate_password_hash


def register(username, password):
    hash_value = generate_password_hash(password)
    try:
        query = text("INSERT INTO users (username,password) VALUES (:username,:password)")
        db.session.execute(query, {"username":username, "password":hash_value})
        db.session.commit()
    except:
        return False
    return login(username, password)

def login(username, password):
    query = text("SELECT id, password FROM users WHERE username=:username")
    result = db.session.execute(query, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            return True
        else:
            return False
        
def user_id():
    return session.get("user_id",0)

def logout():
    del session["user_id"]

def add_plant(name, latinname, light, water, other):
    try:
        query = text("INSERT INTO plants (name, latinname, light, water, other) VALUES (:name, :latinname, :light, :water, :other)")
        db.session.execute(query, {"name":name, "latinname":latinname, "light":light, "water":water, "other":other})
        db.session.commit()
    except:
        return False
    return True

def count_plants():
    query = text("SELECT MAX(id) FROM plants")
    result = db.session.execute(query, {"id":id})
    count = result.fetchone()
    count = count[0]
    if not count:
        return 0
    else:
        return count

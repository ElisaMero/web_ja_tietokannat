
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
        return False
        
def user_id():
    return session.get("user_id",0)

def logout():
    del session["user_id"]

def add_plant(name, latinname, light, water, other):
    try:
        query = text("INSERT INTO plant (name, latinname, light, water, other, user_id) VALUES (:name, :latinname, :light, :water, :other, :user_id)")
        db.session.execute(query, {"name":name, "latinname":latinname, "light":light, "water":water, "other":other, "user_id":session["user_id"]})
        db.session.commit()
        plant_table2(name)
    except:
        return False
    return True

def plant_table2(name):
    try:
        query = text("INSERT INTO plantheadings (name, user_id) VALUES (:name, :user_id)")
        db.session.execute(query, {"name":name, "user_id":session["user_id"]})
        db.session.commit()
    except:
        return False
    return True

def count_plants():
    query = text("SELECT count(*) FROM plant WHERE user_id = :id")
    result = db.session.execute(query, {"id":session["user_id"]})
    count = result.fetchone()
    count = count[0]
    if not count:
        return 0
    return count
    
def show_user():
    query = text("SELECT username FROM users WHERE id = :id")
    result = db.session.execute(query, {"id":session["user_id"]})
    name = result.fetchone()
    name = name[0]
    return name

def plant_headings():
    query = text("SELECT name FROM plantheadings WHERE user_id=:id")
    result = db.session.execute(query, {"id":session["user_id"]})
    info = result.fetchall()
    if info == []:
        return " "
    else:
        info2 = []
        for i in info:
            info2.append(i[0])
        return info2

def plant_info(name):
    query = text("SELECT * FROM plant WHERE user_id =:id AND name =:name")
    result = db.session.execute(query, {"id":session["user_id"], "name":name})
    info = result.fetchall()
    if info == []:
        return " "
    return info

def add_notes(comment, name):
    try:
        query = text("INSERT INTO note1 (comment, user_id, name) VALUES (:comment, :user_id, :name)")
        db.session.execute(query, {"comment":comment, "user_id":session["user_id"], "name":name})
        db.session.commit()
    except:
        return False
    return True



def get_comments(kasvinimi):
    comment = text("SELECT comment FROM note1 WHERE user_id =:id AND name =:name")
    result = db.session.execute(comment, {"id":session["user_id"], "name":kasvinimi})
    info = result.fetchall()
    if info == []:
        return " "
    clean_info = []
    for i in info:
        clean_info.append(i[0])
    return clean_info

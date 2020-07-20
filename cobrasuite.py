from flask import Flask, render_template, url_for, request, session, redirect, jsonify
from flask_pymongo import PyMongo
import hashlib

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/cobra_db"
app.config["MONGO_DBNAME"] = "cobra_db"
mongo = PyMongo(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    if 'login' in session:
        return render_template("search.html")
    else:
        return render_template("login.html")

@app.route("/login", methods=['POST'])
def login():
    users = mongo.db.users
    log_user = users.find_one({'login':request.form['inputLogin']})
    if log_user:
        # check if paswwords are identical
        if hashlib.md5(request.form['inputPassword'].encode('utf-8')).hexdigest() == log_user['pwd']:
            session['login'] = request.form['inputLogin']
            return redirect(url_for('search'))

    return render_template("invalid.html")

@app.route("/cobrarest/mappings", methods=['GET'])
def mappings():
    # if 'login' in session:
    mappings = mongo.db.full_mappings
    all_mappings = mappings.find()
    output = []
    for m in all_mappings:
        output.append({ 'species': m['species'] })
    return jsonify({ 'results': output })

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/account")
def account():
    # user is connect
    if 'login' in session:
        users = mongo.db.users
        log_user = users.find_one({'login':session['login']})
        return render_template("account.html", user=log_user)
    # user not connected
    return render_template("login.html")

@app.route("/disconnect", methods=['POST'])
def disconnect():
    # remove the login from the session if it is there
    session.pop('login')
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, url_for, request, session, redirect
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

@app.route("/search/result/<protein>")
def search_result():
    return render_template("search-result.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/account")
def account():
    return render_template("account.html")

if __name__ == "__main__":
    app.run(debug=True)

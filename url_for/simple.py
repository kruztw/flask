from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/<path:path>")
def others(path):
    # url_for(<function name>) => return route path of that function
    # e.g.
    # url_for('home') => '/'
    return redirect(url_for('home'))

@app.route("/")
def home():
    return "home"

app.run()

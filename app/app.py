from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.before_first_request
def constructor():
    print("call constructor")


@app.route("/", methods=["GET"])
def home():
    return "home"




app.run()

from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)

#CORS(app)                                                                                      # 允許所有來源
#CORS(app, resources={r"/.*": {"origins": ["http://localhost:8888","http://www.example.com"]}}) # 允許特定來源

@app.route("/")
def helloWorld():
  return "Hello! from home"

@app.route("/cors")
@cross_origin()                     # 允許所有來源
def cors():
  return "from cors hello"

app.run()

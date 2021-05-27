from flask import Flask, Response
import requests

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route("/<path:path>")   # 只有這行的話 localhost:5000/ 不會進來
def others(path):
    print("path = ", path)
    r = requests.get("http://127.0.0.1:3000/"+path)
    headers = [(name, value) for (name, value) in r.raw.headers.items()]
    res = Response(r.content, r.status_code, headers)
    return res

app.run()

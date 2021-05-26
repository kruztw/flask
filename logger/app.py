from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    app.logger.debug('A value for debugging')
    app.logger.warning('A warning occurred (%d apples)', 42)
    app.logger.error('An error occurred')
    return "Hello world!";


app.debug = True # 沒加這行 app.logger.debug 不會顯示
app.run()

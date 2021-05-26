from flask import Flask, request, render_template_string

app = Flask(__name__)

app.config['method1'] = True

app.method2 = True

app.config.update(method3=True, method4=True)

print(app.config)

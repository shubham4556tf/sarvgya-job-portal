from flask import Flask

app = Flask(__name__)

app.route("/")
def hello_world():
    return "<p>this is the test funtion</p>"
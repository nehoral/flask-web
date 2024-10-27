from flask import Flask

app = Flask(__name__)

@app.route("/")
def flask_web():
    return "<p>flask web app</p>"

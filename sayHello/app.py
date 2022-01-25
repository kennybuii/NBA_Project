from flask import Flask, render_template, request, flash

app = Flask(__name__)
#test
@app.route("/hello")
def index():
    return render_template("index.html")
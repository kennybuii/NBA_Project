from distutils.log import debug
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"
#test123
@app.route("/hello")
def index():
    flash("what's your name?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("HI " + str(request.form['name_input']) + ", great to see you!")
    return render_template("index.html")

@app.route("/members")
def members():
    return {"members": ["Member1", "Member2", "Member3"]}

if __name__== "__main__":
    app.run(debug=True)

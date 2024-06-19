import time
from flask import Flask , redirect, url_for  # type: ignore
app = Flask(__name__)


@app.route("/")
def home():
    return "<h1> Welcome to the Aditya Vardhan's Page </h1>"


@app.route("/pass")
def passed():
    return "<H1> CongratZ , You have passed the Exam. </h1>"

@app.route("/fail")
def failed():
    return "<H1> Sorry, You have failed in the Exam .</h1>"


@app.route("/score/<name>/<int:num>")
def score(name,num):
    if num < 30:
        time.sleep(1)
        return redirect(url_for("failed"))
    else :
        time.sleep(1)
        return redirect(url_for("passed"))

if __name__ == "__main__":
    app.run(debug=True)

# Developer : Mr. Aditya Vardhan (Instagram) @aditya__vardhan__ 
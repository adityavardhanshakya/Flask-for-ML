import time
from flask import Flask , redirect, url_for  # type: ignore
app = Flask(__name__)


@app.route("/")
def home():
    return "<h1> Welcome to the Aditya Vardhan's Page </h1>"


@app.route("/pass/<sname>/<int:marks>")
def passed(sname,marks):
    return f"<H1> CongratZ {sname.title()}, You have passed the Exam with {marks}. </h1>"

@app.route("/fail/<sname>/<int:marks>")
def failed(sname,marks):
    return f"<H1> Sorry {sname.title()}, You have failed in the Exam with {marks}.</h1>"


@app.route("/score/<name>/<int:num>")
def score(name,num):
    if num < 30:
        time.sleep(1)
        return redirect(url_for("failed", sname=name, marks=num ))
    else :
        time.sleep(1)
        return redirect(url_for("passed", sname=name, marks=num ))

if __name__ == "__main__":
    app.run(debug=True)

# Developer : Mr. Aditya Vardhan (Instagram) @aditya__vardhan__ 
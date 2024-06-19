from flask import Flask 

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>welcome to the first page baby </h1>"

@app.route("/about")
def about():
    return "<h1>welcome to the about page baby </h1>"


@app.route("/welcome/<name>")
def welcome(name):
    return f"<h1>welcome {name.title()}, On this Page Baby </h1>"


@app.route("/addition/<int:num>")
def addition(num):
    return f"<h1>the sum of {num} is {num + 20} </h1>"

@app.route("/addition_2/<int:num1>//<int:num2>")
def addition_2(num1,num2):
    return f"<h1>the sum of {num1} and {num2} is {num1+num2} </h1>"



if __name__ == "__main__":
    app.run(debug=True)
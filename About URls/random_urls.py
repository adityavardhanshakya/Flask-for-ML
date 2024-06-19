from flask import Flask  # type: ignore
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Welcome to the my page </h1>"

@app.route("/welcome/<name>")
def welcome(name):
    return f"<H3>Hello {name.title()}, How are you my Friend ?</h3>"

if __name__ == "__main__":
    app.run(debug=True)



# Developer : Mr. Aditya Vardhan (Instagram) @aditya__vardhan__ 
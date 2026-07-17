from flask import Flask,redirect,url_for


app = Flask(__name__)
@app.route("/")
def home():
    return "hello <h1>hello<h1> " 


@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/admi")
def admi():
    return redirect(url_for("user",name="Admi!"))

if __name__=="__main__":
    app.run()
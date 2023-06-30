from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_object("config")
app.config.from_pyfile("config.py")


@app.route('/')
def index():
    return "<h1>Hello World!</h1>"

# app.add_url_rule("/","index",index)

@app.route("/user/<name>")
def user(name: str):
    return "<h1>Hello, {}!</h1>".format(name)

@app.route("/user1/<name>")
def user1(name):
    return "<h1>Bye, {}!</h1>".format(name)
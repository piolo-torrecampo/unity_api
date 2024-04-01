from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello World</p>"

{
    "object": ,
    "rotation": "360",
    "scale": "double",
    "position": "beside"
}
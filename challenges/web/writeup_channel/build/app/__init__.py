from flask import Flask, render_template, request
from datetime import datetime
from .messages import init_messages, Message

app = Flask(__name__)
app.config["MESSAGES"] = init_messages()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        message = request.form["message"]
        app.config["MESSAGES"].append(Message(
            "感谢投稿！<br>" + message, datetime.now().strftime("%H:%M")
        ))
    return render_template("index.html", messages=app.config["MESSAGES"])

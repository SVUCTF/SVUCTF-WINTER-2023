import secrets
from typing import List
from flask import (
    Flask,
    redirect,
    jsonify,
    render_template,
    request,
    session,
    url_for,
    make_response,
)
from .config import Config
from .utils import captcha_image, random_code, random_password

app = Flask(__name__)
app.config.from_object(Config())


class User:
    def __init__(self, username: str, email: str, password: str, reset_code: str):
        self.username = username
        self.email = email
        self.password = password
        self.reset_code = reset_code


USERS: List[User] = [
    User("admin", "admin@svuctf.com", secrets.token_hex(16), secrets.token_hex(8))
]


@app.route("/")
def index():
    return redirect(url_for("home"))


@app.route("/home")
def home():
    if session.get("user") == "admin":
        return render_template("home.html", flag=app.config["FLAG"])
    else:
        return redirect(url_for("login"))


@app.route("/auth/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        captcha = request.form["captcha"]

        if captcha.lower() != session["captcha"].lower():
            return render_template("login.html", message="Invalid CAPTCHA")

        if user := next(
            (u for u in USERS if u.username == username and u.password == password),
            None,
        ):
            session["user"] = user.username
            return redirect(url_for("home"))
        else:
            return render_template(
                "login.html",
                message="The username or password you entered is incorrect",
            )

    return render_template("login.html")


@app.route("/auth/password/forget", methods=["GET", "POST"])
def forget():
    if request.method == "POST":
        email = request.form["email"]
        user_code = request.form["code"]

        if user := next((u for u in USERS if u.email == email), None):
            if user.reset_code == user_code:
                new_password = random_password()
                user.password = new_password
                return render_template(
                    "forget.html",
                    message=f"Password reset successfully! Your new password is: {new_password}",
                )

        return render_template(
            "forget.html", message="Invalid email or code", error=True
        )

    return render_template("forget.html")


@app.route("/auth/password/forget/send_code", methods=["POST"])
def send_code():
    email = request.form["email"]

    if user := next((u for u in USERS if u.email == email), None):
        user.reset_code = random_code(8)
        return jsonify({"success": True, "message": "Code sent successfully"})
    else:
        return jsonify({"success": False, "message": "Email does not exist"})


@app.route("/auth/captcha/image/<key>")
def captcha_img(key: str):
    captcha, image = captcha_image(key)
    session["captcha"] = captcha

    response = make_response(image)
    response.headers.set("Content-Type", "image/jpeg")

    return response

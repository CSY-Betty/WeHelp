from flask import *

app = Flask(__name__, static_folder="static", static_url_path="/")

app.secret_key = "This is Week 4."


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signin", methods=["POST"])
def signin():
    username = request.form["username"]
    password = request.form["password"]
    if username == "test" and password == "test":
        session["username"] = username
        return redirect("/member")
    else:
        # return redirect("/error?message=Username or password is not correct.")
        return redirect(
            url_for("error", message="Username or password is not correct.")
        )


@app.route("/signout")
def signout():
    del session["username"]
    return redirect("/")


@app.route("/member")
def member():
    if "username" in session:
        return render_template("member.html")
    else:
        return redirect("/")


@app.route("/error")
def error():
    message = request.args.get("message", "發生錯誤，請聯繫客服！")
    return render_template("error.html", message=message)


@app.route("/calculate")
def calc():
    positive = int(request.args.get("positive"))
    return redirect(url_for("result", positive=positive))


@app.route("/square/<int:positive>")
def result(positive):
    result = positive**2
    return render_template("square.html", result=result)


app.run(port=3000)

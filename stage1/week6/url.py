from flask import *
from dbcrud import *

app = Blueprint("route", __name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/signup", methods=["POST"])
def signup():
    name = request.form["name"]
    username = request.form["username"]
    password = request.form["password"]

    if check_duplicate_username(username):
        return redirect(url_for("route.error", message="帳號已經被註冊"))
    else:
        insert_member(name, username, password)
        return redirect("/")


@app.route("/signin", methods=["POST"])
def signin():
    username = request.form["username"]
    password = request.form["password"]
    if check_member(username, password):
        name = get_name(username, password)
        member_id = get_memberid(username, password)
        session["name"] = name
        session["member_id"] = member_id
        return redirect("/member")

    return redirect(url_for("route.error", message="帳號或密碼輸入錯誤"))


@app.route("/signout")
def signout():
    del session["name"]
    del session["member_id"]
    return redirect("/")


@app.route("/member")
def member():
    name = session.get("name")
    if name is not None:
        messages = get_message()
        return render_template("member.html", name=name, messages=messages)
    else:
        return redirect("/")


@app.route("/error")
def error():
    message = request.args.get("message", "發生錯誤，請聯繫客服！")
    return render_template("error.html", message=message)


@app.route("/createMessage", methods=["POST"])
def createMessage():
    member_id = session.get("member_id")
    message = request.form["message"]

    add_message(member_id, message)
    return redirect("/member")


@app.route("/deleteMessage", methods=["POST"])
def deleteMessage():
    message = request.form["deletemessage"]

    remove_message(message)
    return redirect("/member")

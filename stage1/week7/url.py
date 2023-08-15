from flask import *
from dbcrud import *
import json

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


@app.route("/api/member", methods=["GET"])
def search_username():
    username = request.args.get("username")
    result = search_member(username)
    if result:
        id_value, name_value, username_value = result
        data_dict = {"id": id_value, "name": name_value, "username": username_value}
    else:
        data_dict = None  # Null

    result_dict = {"data": data_dict}
    return jsonify(result_dict)


@app.route("/api/member", methods=["PATCH"])
def update_name():
    data = request.json
    new_name = data.get("name")
    member_id = session.get("member_id")
    print(new_name, member_id)

    result = update_name_todb(member_id, new_name)

    if result:
        session["name"] = new_name
        result_dict = {"ok": True}
    else:
        result_dict = {"error": True}

    return jsonify(result_dict)

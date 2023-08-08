from flask import *
import mysql.connector

app = Flask(__name__, static_folder="static", static_url_path="/")

app.secret_key = "This is Week 6."

# connect to sql
mydb = mysql.connector.connect(
    host="localhost", user="root", password="root123", database="website"
)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


def check_duplicate_username(username):
    with mydb.cursor() as cursor:
        sql = "SELECT username FROM member WHERE username = %s"
        cursor.execute(sql, (username,))
        result = cursor.fetchone()
        return result is not None


@app.route("/signup", methods=["POST"])
def signup():
    name = request.form["name"]
    username = request.form["username"]
    password = request.form["password"]

    if check_duplicate_username(username):
        return redirect(url_for("error", message="帳號已經被註冊"))

    with mydb.cursor() as cursor:
        sql = "INSERT INTO member(name, username, password) VALUES(%s, %s, %s)"
        cursor.execute(
            sql,
            (
                name,
                username,
                password,
            ),
        )

        mydb.commit()

    return redirect("/")


def check_member(username, password):
    with mydb.cursor() as cursor:
        sql = "SELECT username FROM member WHERE username = %s AND password = %s"
        cursor.execute(sql, (username, password))
        result = cursor.fetchone()
        return result is not None


def get_name(username, password):
    with mydb.cursor() as cursor:
        sql = "SELECT name FROM member WHERE username = %s AND password = %s"
        cursor.execute(sql, (username, password))
        result = cursor.fetchone()
        name = result[0]
        return name


def get_memberid(username, password):
    with mydb.cursor() as cursor:
        sql = "SELECT id FROM member WHERE username = %s AND password = %s"
        cursor.execute(sql, (username, password))
        result = cursor.fetchone()
        name = result[0]
        return name


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

    return redirect(url_for("error", message="帳號或密碼輸入錯誤"))


@app.route("/signout")
def signout():
    del session["name"]
    del session["member_id"]
    return redirect("/")


def get_message():
    with mydb.cursor() as cursor:
        sql = "SELECT member.name, message.content FROM message RIGHT JOIN member on message.member_id = member.id"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result


@app.route("/member")
def member():
    name = session.get("name")
    if name is not None:
        messages = get_message()
        messages.reverse()
        return render_template("member.html", name=name, messages=messages)
    else:
        return redirect("/")


@app.route("/error")
def error():
    message = request.args.get("message", "發生錯誤，請聯繫客服！")
    return render_template("error.html", message=message)


@app.route("/createMessage", methods=["POST"])
def createMessage():
    name = session.get("name")
    member_id = session.get("member_id")
    message = request.form["message"]

    with mydb.cursor() as cursor:
        sql = "INSERT INTO message(member_id, content) VALUES(%s, %s)"
        cursor.execute(sql, (member_id, message))
        mydb.commit()

    return redirect("/member")


app.run(port=3000)

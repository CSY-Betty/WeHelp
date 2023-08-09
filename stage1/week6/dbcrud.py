import mysql.connector

# connect to sql
mydb = mysql.connector.connect(
    host="localhost", user="root", password="root123", database="website"
)


def excute_sql_one(sql, *args):
    with mydb.cursor() as cursor:
        cursor.execute(sql, args)
        return cursor.fetchone()


def excute_sql_all(sql, *args):
    with mydb.cursor() as cursor:
        cursor.execute(sql, args)
        return cursor.fetchall()


def check_duplicate_username(username):
    sql = "SELECT username FROM member WHERE username = %s"
    result = excute_sql_one(sql, username)
    return result is not None


def insert_member(name, username, password):
    sql = "INSERT INTO member(name, username, password) VALUES(%s, %s, %s)"
    excute_sql_all(sql, name, username, password)
    mydb.commit()


def check_member(username, password):
    sql = "SELECT username FROM member WHERE username = %s AND password = %s"
    result = excute_sql_one(sql, username, password)
    return result is not None


def get_name(username, password):
    sql = "SELECT name FROM member WHERE username = %s AND password = %s"
    result = excute_sql_one(sql, username, password)
    name = result[0]
    return name


def get_memberid(username, password):
    sql = "SELECT id FROM member WHERE username = %s AND password = %s"
    result = excute_sql_one(sql, username, password)
    name = result[0]
    return name


def get_message():
    sql = "SELECT member.name, message.content FROM message RIGHT JOIN member on message.member_id = member.id ORDER BY message.time DESC"
    result = excute_sql_all(sql)
    return result


def add_message(member_id, message):
    sql = "INSERT INTO message(member_id, content) VALUES(%s, %s)"
    excute_sql_all(sql, member_id, message)
    mydb.commit()


def remove_message(message):
    sql = "DELETE FROM message WHERE content = %s"
    excute_sql_all(sql, message)
    mydb.commit()

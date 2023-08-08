import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="root123", database="website"
)

with mydb.cursor() as cursor:
    sql = "SELECT member.name, message.content FROM message RIGHT JOIN member on message.member_id = member.id"
    cursor.execute(sql)
    result = cursor.fetchall()
for name, message in result:
    print(name, message)

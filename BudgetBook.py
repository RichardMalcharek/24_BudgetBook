import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456"
)

my_cursor = my_db.cursor()

dbName = "budgetbook"

my_cursor.execute(f"CREATE DATABASE {dbName}")

my_cursor.execute("SHOW DATABASES")

for db in my_cursor:
    print(db)
import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="moz.codde",
        database="alx_book_store",
    )
except mysql.connector.Error:
    print("Error: Failed to connect to the DB")

my_cursor = mydb.cursor()

my_cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
print("Database 'alx_book_store' created successfully!")



my_cursor.close()
mydb.close()
# import mysql.connector
# dataBase =mysql.connector.connect(
#     host ='localhost',
#     user = 'root',
#     passwd = 'gere23',
# )

# curser = dataBase.cursor()

# curser.execute("create database geredjango")
# print("all are done!")
import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'gere23'

	)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE geredjango")

print("All Done!")
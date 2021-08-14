import sqlite3

connection = sqlite3.connect("database.db")

with open('schema.sql') as f:
	connection.executescript(f.read())

connection.commit()
connection.close()

# creates database.db file and runs scripts in schema.sql creating the urls table
# see here: https://flask.palletsprojects.com/en/2.2.x/patterns/sqlite3/
# see here: https://docs.python.org/3/library/sqlite3.html#sqlite3-tutorial
import sqlite3
from flask import Flask
from flask import g
import shutil

app = Flask(__name__)
DATABASE = "./database.db"
def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = sqlite3.connect(DATABASE)
	return db
# see here: https://flask.palletsprojects.com/en/2.2.x/appcontext/
# should not need to call this manually
@app.teardown_appcontext
def close_connection(mydb):
	db = getattr(g, '_database', None)
	if db is not None:
		db.close()
def setup_database(mydb):
	mycursor = mydb.cursor()
	mycursor.execute("CREATE TABLE IF NOT EXISTS customers (name VARCHAR(255), address VARCHAR(255))")
def delete_database(mydb):
	mycursor = mydb.cursor()
	mycursor.execute("DROP TABLE IF EXISTS customers")
	mydb.commit()
def read_from_database(mydb):
	mycursor = mydb.cursor()
	res = mycursor.execute("SELECT * FROM customers")
	return res.fetchall()
def write_to_database(mydb,name,addr):
	mycursor = mydb.cursor()
	mycursor.execute("INSERT INTO customers (name, address) VALUES (?, ?)",(name,addr))
	mydb.commit()
def delete_entry_from_database(mydb,name):
	mycursor = mydb.cursor()
	mycursor.execute("DELETE FROM customers WHERE name=(?)",(name,))
	mydb.commit()
def backup_database_to_disk(db_name,out_name):
	shutil.copyfile(db_name,out_name)
# need to add commands for backing up databases
def print_commands():
	print("Press:")
	print("\t- P to print the table.")
	print("\t- ? to list these commands again.")
	print("\t- I to input values to the table.")
	print("\t- D to delete entries.")
	print("\t- B backup database to file.")
	print("\t- E to end your session.")

# a driver function to showcase functionality of the database functions in this file
def main():
	# need an app context in flask to use get_db
	# this is supposed to be done automatically for our decorated flask functions I think
	with app.app_context():
		db_name = "./database.db"
		# connect to the mysql server on the localhost with user name john and password secret
		mydb = get_db()
		# create a database called mydatabase with a table containing columns for names/addresses
		setup_database(mydb)
		# loop to show library functionality
		inStr = ""
		print_commands()
		while inStr != "E":
			inStr = input(">")
			if inStr == "I":
				write_to_database(mydb,input("Please enter a name to input:"),input("Please enter an address to input:"))
			elif inStr == "P":
				print("Table contents:")
				print(read_from_database(mydb))
			elif inStr == "?":
				print_commands()
			elif inStr == "D":
				delete_entry_from_database(mydb,input("Please enter a name to delete by:"))
			elif inStr == "E":
				print("Goodbye.")
			elif inStr == "B":
				backup_database_to_disk(db_name,input("Please enter a filename to backup the current database to:"))
			else:
				print("Invalid input.")
if __name__ == "__main__":
	main()

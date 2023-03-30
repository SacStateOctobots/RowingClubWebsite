import mysql.connector
import os
import subprocess
from subprocess import Popen, PIPE
import shlex

# connecting to the database will look roughly like this. This returns a value that must be passed as mydb 
# in the functions below. We can hardcode the host and the user most likely. We will need to figure
# out how to handle the password securely.
def connect_to_database():
	# can also do
	# return mysql.connector.connect(host="localhost",user="john",password="secret", database="somedatabase")
	return mysql.connector.connect(host="localhost",user="john",password="secret")
# closes the connection created by connect_to_database.
def disconnect_from_database(mydb):
	mydb.close()
# setting up the database will look like this. We will need to populate this with all the required 
# fields to hold the data needed by the client. This should only be used very carefully.
def setup_database(mydb):
	mycursor = mydb.cursor()
	mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
	mycursor.execute("USE mydatabase")
	mycursor.execute("CREATE TABLE IF NOT EXISTS customers (name VARCHAR(255), address VARCHAR(255))")
# deleting the database looks like this. This should only be used very carefully.
def delete_database(mydb):
	mycursor = mydb.cursor()
	mycursor.execute("DROP TABLE IF EXISTS customers")
	mycursor.execute("DROP DATABASE IF EXISTS mydatabase")
# we will add different read functions of this form based on whatever data needs to be read from the
# database.
def read_from_database(mydb):
	mycursor = mydb.cursor()
	mycursor.execute("SELECT * FROM customers")
	return mycursor.fetchall()
# we will add different write functions of this form based on whatever data needs to be written to the
# database.
def write_to_database(mydb,name,addr):
	mycursor = mydb.cursor()
	mycursor.execute("INSERT INTO customers (name, address) VALUES (%s, %s)",(name,addr))
	mydb.commit()
# we will add different delete functions of this form based on whatever data needs to be deleted from the
# database.
# This also has sql injection issues I think. We should probably use the syntax shown in write_to_database here
def delete_entry_from_database(mydb,name):
	mycursor = mydb.cursor()
	mycursor.execute("DELETE FROM customers WHERE name='"+name+"'")
#I need to do more research on these to figure out how exactly we should be reading/writing to the disk.
def write_database_to_disk():
	# Prompts for the root account password for db.
	# there may be a safer way to do this than calling it via a subprocess.
	# doing this via root rather than some other account may not be ideal.
	subprocess.call(shlex.split('mysqldump -u root -p mydatabase --result-file=database_backup.sql'))
def load_database_from_disk(mydb,fname):
	# Also prompts for root account password for db.
	# Same issues as before.
	if os.path.isfile(fname):
		mycursor = mydb.cursor()
		mycursor.execute("DROP DATABASE IF EXISTS mydatabase")
		mycursor.execute("CREATE DATABASE mydatabase")
		mycursor.execute("USE mydatabase")
		process = Popen(['mysql', 'mydatabase', '-u', 'root', '-p'],stdout=PIPE, stdin=PIPE)
		output = process.communicate(str.encode('source ' + fname))[0]
	else:
		print("Database file "+fname+"does not exist in working directory.")

def print_commands():
	print("Press:")
	print("\t- P to print the table.")
	print("\t- ? to list these commands again.")
	print("\t- I to input values to the table.")
	print("\t- D to delete entries.")
	print("\t- W to dump the database to the disk.")
	print("\t- L to load a database from the disk.")
	print("\t- E to end your session.")

# a driver function to showcase functionality of the database functions in this file
def main():
	# connect to the mysql server on the localhost with user name john and password secret
	mydb = connect_to_database()
	# create a database called mydatabase with a table containing columns for names/addresses
	setup_database(mydb)
	# loop to show library functionality
	mycursor = mydb.cursor()
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
		elif inStr == "W":
			write_database_to_disk()
		elif inStr == "L":
			load_database_from_disk(mydb,input("Enter a database file to load:"))
		else:
			print("Invalid input.")
	# delete the database
	delete_database(mydb)
	#close the connection
	disconnect_from_database(mydb)

if __name__=="__main__":
	main()
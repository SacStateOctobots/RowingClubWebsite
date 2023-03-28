import database_library_demo as db

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
	mydb = db.connect_to_database()
	# create a database called mydatabase with a table containing columns for names/addresses
	db.setup_database(mydb)
	# loop to show library functionality
	mycursor = mydb.cursor()
	inStr = ""
	print_commands()
	while inStr != "E":
		inStr = input(">")
		if inStr == "I":
			db.write_to_database(mydb,input("Please enter a name to input:"),input("Please enter an address to input:"))
		elif inStr == "P":
			print("Table contents:")
			print(db.read_from_database(mydb))
		elif inStr == "?":
			print_commands()
		elif inStr == "D":
			db.delete_entry_from_database(mydb,input("Please enter a name to delete by:"))
		elif inStr == "E":
			print("Goodbye.")
		elif inStr == "W":
			db.write_database_to_disk()
		elif inStr == "L":
			db.load_database_from_disk(mydb,input("Enter a database file to load:"))
		else:
			print("Invalid input.")
	# delete the database
	db.delete_database(mydb)
	#close the connection
	db.disconnect_from_database(mydb)

if __name__=="__main__":
	main()

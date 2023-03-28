import database_library_demo as db

# connect and delete the database from mysql then disconnect
def main():
	mydb = db.connect_to_database()
	db.setup_database(mydb)
	db.disconnect_from_database(mydb)

if __name__=="__main__":
	main()

import mysql.connector

def main():
	# connect to the mysql server on the localhost with user name john and password secret
	mydb = mysql.connector.connect(host="localhost",user="john",password="secret")
	print(mydb) 
	# create a database called mydatabase with a table containing columns for names/addresses
	mycursor = mydb.cursor()
	mycursor.execute("CREATE DATABASE mydatabase")
	mycursor.execute("USE mydatabase")
	mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
	# loop 
	inStr = ""
	while inStr != "E":
		inStr = input("Press P to print the table, I to input values to the table or E to end:")
		if inStr == "I":
			name  = input("Please enter a name:")
			addr = input("Please enter an address:")
			mycursor.execute("INSERT INTO customers (name, address) VALUES (%s, %s)",(name,addr))
			mydb.commit()
		elif inStr == "P":
			print("Table contents:")
			mycursor.execute("SELECT * FROM customers")
			myresult = mycursor.fetchall()
			for x in myresult:
				print(x)
		else:
			print("Invalid input.")
	# cleanup
	mycursor.execute("DROP TABLE IF EXISTS customers")
	mycursor.execute("DROP DATABASE mydatabase")

if __name__=="__main__":
	main()

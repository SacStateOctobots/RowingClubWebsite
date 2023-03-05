See here:
	- https://www.w3schools.com/python/python_mysql_getstarted.asp
To run the demo (on linux):
	1. Install mysql.
	2. Run mysql.
		- Do "sudo mysql"
	3. Create a dummy user john with the password 'secret'.
		- Do this with "CREATE USER 'john'@'localhost' IDENTIFIED BY 'secret';"
		- You can view users with "select user from mysql.user;"
		- You can delete the user created above with "DROP USER 'john'@'localhost';"
	4. Give the newly created user full permissions.
		- Do this with "GRANT ALL PRIVILEGES ON *.* TO 'sammy'@'localhost' WITH GRANT OPTION;"
	5. Run the python script.
		- Do python3 database_demo.py

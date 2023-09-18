import os
import database_library as db
try:
	print("Removing database file "+db.DATABASE+" created from schema file "+db.SCHEMA+".")
	# delete the database file
	os.remove(db.DATABASE)
except:
	print("Exception: database.db file does not exist. Continuing...")
# delete the image uploads directory
print("Clearing ./static/image_uploads directory:")
for f in os.listdir("static/image_uploads"):
	print("\t"+f)
	try:
		os.remove("./static/image_uploads/"+f)
	except:
		print("Exception: Cannot remove ./static/image_uploads/"+f+". continuing...")

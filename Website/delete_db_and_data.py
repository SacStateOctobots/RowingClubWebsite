import os
import database_library as db
print("Removing database file "+db.DATABASE+" created from schema file "+db.SCHEMA+".")
# delete the database file
os.remove(db.DATABASE)
# delete the image uploads directory
print("Clearing ./static/image_uploads directory:")
for f in os.listdir("static/image_uploads"):
	print("\t"+f)
	os.remove("./static/image_uploads/"+f)

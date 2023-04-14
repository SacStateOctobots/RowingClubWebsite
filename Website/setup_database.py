import database_library as db
print("Creating database file "+db.DATABASE+" from schema file "+db.SCHEMA+".")
print("Rerunning this script does not delete or reset local files.")
# set up the database from the schema file
db.init_db()

# copy the default pfp images into the ./static/image_uploads directory
from distutils.dir_util import copy_tree
copy_tree("default_images", "static/image_uploads")

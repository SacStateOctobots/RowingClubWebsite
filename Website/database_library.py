# see here: https://flask.palletsprojects.com/en/2.2.x/patterns/sqlite3/
# see here: https://docs.python.org/3/library/sqlite3.html#sqlite3-tutorial
import sqlite3
from flask import Flask
from flask import g
import shutil

app = Flask(__name__)
DATABASE = "./database.db"
SCHEMA = "./schema.sql"
# returns a connection to the database file
def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = sqlite3.connect(DATABASE)
	return db
# returns a connection to the database file
# this is not intended to be ran while flask is running
def get_db_no_flask():
	return sqlite3.connect(DATABASE)
# see here: https://flask.palletsprojects.com/en/2.2.x/appcontext/
# you should not need to call this manually
@app.teardown_appcontext
def close_connection(mydb):
	db = getattr(g, '_database', None)
	if db is not None:
		db.close()
# backup the database file to another file
def backup_database_to_disk(db_name,out_name):
	shutil.copyfile(db_name,out_name)
# query function from sqlite+flask docs above
def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv
def insert_to_db(table_str,column_str,valfmt_str,vals):
	cur = sqlite3.connect(DATABASE)
	cur.execute("INSERT INTO "+table_str+" "+column_str+" VALUES "+valfmt_str,vals)
	cur.commit()
def delete_from_db(table_str,column_str,vals):
	cur = sqlite3.connect(DATABASE)
	cur.execute("DELETE FROM "+table_str+" WHERE "+column_str+"=(?)",(vals,))
	cur.commit()
# builds the database from the schema file schema.sql
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource(SCHEMA, mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
#######################################################
# sample player table handling functions
#######################################################
def get_players():
	return query_db('select * from players')
def insert_player(name,desc,filename):
	#runs cur.execute("INSERT INTO players (name, description,imgfilename) VALUES (?, ?)",(name,desc,imgfile))
	insert_to_db("players","(name,description,imgfilename)","(?,?,?)",(name,desc,filename))
def delete_player(name):
	#runs cur.execute("DELETE FROM players WHERE name=(?)",(name,))
	delete_from_db("players","name",name)

#######################################################
# alumni table functions
#######################################################
def get_alumni():
	return query_db('select * from alumni')
def insert_alumni(name,desc,filename):
	insert_to_db("alumni","(name,description,imgfilename)","(?,?,?)",(name,desc,filename))
def delete_alumni(name):
	delete_from_db("alumni","name",name)

#######################################################
# team_members table
#######################################################
def get_team_members():
	return query_db('select * from team_members')
def insert_team_members(name, team_member, imgfilename,role):
	insert_to_db("team_members","(name, team_member, imgfilename, role)","(?,?,?,?)", (name, team_member, imgfilename, role))
def delete_testemonial(name):
	delete_from_db("team_members","name",name)
#def delete_database(mydb):
	#mycursor = mydb.cursor()
	#mycursor.execute("DROP TABLE IF EXISTS customers")
	#mydb.commit()

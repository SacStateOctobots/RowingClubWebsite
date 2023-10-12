import flask
import flask_login
import os
from flask import Flask, flash, render_template, current_app, request, redirect, session
from flask_mail import Mail, Message
from werkzeug.utils import secure_filename
import google_calendar_reader as cal
import database_library as db
import random

app = flask.Flask(__name__)
app.secret_key = 'super secret string'  # Change this!

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

# Our mock databases.
# irl we should use an actual database for this.
# We would also obviously not want to store username/login info in plain text like this.
users = {'foo@bar.tld': {'pw': 'secret'}} #for user login info

# see: https://flask.palletsprojects.com/en/2.2.x/patterns/fileuploads/
# directory where uploaded images will be stored
UPLOAD_FOLDER = 'static/image_uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# set up the mail instance
keyFile = open("EMAIL_KEY", "r")
emailKey = keyFile.read()
keyFile.close()
addressFile = open("EMAIL_ADDRESS", "r")
emailAddress = addressFile.read()
addressFile.close()
app.config.update(
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = emailAddress,
	MAIL_PASSWORD = emailKey
)
mail = Mail(app)

#Passcode for OTP
global_final_otp = ''

class User(flask_login.UserMixin):
    pass

@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user

@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['pw'] == users[email]['pw']

    return user


@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'

#@app.route('/')
#def index():
#    if flask_login.current_user.is_anonymous:
#        return 'Hello anonymous user'
#    else:
#        return f'Hello {flask_login.current_user.id}'
#        #return 'Hello user' 
@app.route("/")
def welcome():
	newEvents = cal.get_next_five_events()
	return render_template("welcome.html",next_events=newEvents)

@app.route("/donate")
def donate():
    return render_template("donate.html")

@app.route("/members")
def members():
    return render_template("members.html", member=db.get_team_members())

@app.route("/alumni")
def alumni():
    return render_template("alumni.html", alumni=db.get_alumni())

@app.route("/calendar")
def calendar():
	oldEvents = cal.get_last_five_events()
	newEvents = cal.get_next_five_events()
	return render_template("calendar.html",past_events = oldEvents,next_events = newEvents)

@app.route("/instagram")
def instagram():
    return render_template("instagram.html")

@app.route("/about")
def about():
    return render_template("about_us.html", officers=db.get_about())

#recruitment page
@app.route("/join")
def join():
    test = db.get_testimonial
    
    return render_template("join.html",test=test)

@app.route("/contact")
def contact():
    return render_template("contactus.html")


@app.route("/contact",methods=['POST'])
def contact_post():
	msg = Message(subject=request.form['subject'],
				body="Hello, \n\n My name is "+request.form['name']+". My email is " + request.form['email']+ 
                        "\n\nHere is my message: "+request.form['message']+"\n\nYou can contact me at: "+request.form['phone']
                                    + "\n\n(Note: There is a message from Contact Page - Sac State Rowing Website)",
                        
				sender=request.form['email'],
				recipients=[emailAddress.rstrip()])
	mail.send(msg)
	return render_template("contactus.html")

@app.route("/recruitment")
def recruitment():
    return render_template("recruitment.html")
 

@app.route('/login', methods=['GET'])
def login():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login_form():
	email = flask.request.form['email']
	if flask.request.form['pw'] == users[email]['pw']:
		user = User()
		user.id = email
		flask_login.login_user(user)
		return flask.redirect(flask.url_for('protected_get'))
	return 'Bad login'
	#return render_template("login.html")

##TO-DO:
#	- find way to make sure code becomes invalid after a set amount of time
#	- check email to make sure it is a valid email addr and that it matches set email
#		-make sure email storage is done with hash value and to validate with hash match
#	- email message needs to be secure, email text should be hidden from traffic sniffing
@app.route('/verify', methods = ["POST"])
def verify(): 
	#Creates OTP
	final_otp = ''
	for i in range(6):
		final_otp = final_otp + str(random.randint(0,9))
	#Sends message to email put in form
	msg = Message(subject="Rowing Club Sign-in Passcode",
				body="Passcode for log-in verification: "
				+ str(final_otp),  
				sender="noreply@rowingclub.com", #curr ver shows sender same as recipient in actal email, see if there is a fix for this
				recipients=[request.form['email_otp']])
	mail.send(msg)
	#Sets a session var to be referenced for validate page. 
	#Might be removed after flask session is ended but not sure how this works with hosted website
	session['final_otp'] = final_otp
	return render_template('login_otp.html') 

@app.route('/validate',methods=["POST"])   
def validate():      
    # OTP Entered by the User
    user_otp = request.form['otp'] 
    print("User OTP : ", user_otp)
     
    if int(session['final_otp']) == int(user_otp):  
        return flask.redirect(flask.url_for('protected_get'))
    else:
        flash('Incorrect Passcode Entered, Try again')
        return render_template('login_otp.html')



@app.route('/protected', methods=['GET'])
@flask_login.login_required
def protected_get():
	return render_template("admin.html", players=db.get_players());

@app.route('/protected', methods=['POST'])
@flask_login.login_required
def protected_post():
	if "delete-form" in request.form:
		text = request.form['deleteplayer']
		db.delete_player(text)
	if "add-form" in request.form:
		nametext = request.form['addname']
		desc = request.form['desc']
		# check if the post request has the file part
		if 'file' not in request.files:
			print('No file part')
			return redirect(request.url)
		file = request.files['file']
		# If the user does not select a file, the browser submits an
		# empty file without a filename.
		if file.filename == '':
			print('No file name')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			print('Success')
			filename = secure_filename(file.filename)
			print(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		else:
			print('File name not allowed')
			return redirect(request.url)
		db.insert_player(nametext,desc,filename)
            
#######################################################
# Alumni form -> needs to be changed to edit text. Alumni memebers not a part of page
#######################################################

	if "alumni-delete-form" in request.form:
		text = request.form['deletealumni']
		db.delete_alumni(text)
	if "alumni-add-form" in request.form:
		nametext = request.form['alumni-addname']
		desc = request.form['alumni-desc']
		# check if the post request has the file part
		if 'alumni-file' not in request.files:
			print('No file part')
			return redirect(request.url)
		file = request.files['alumni-file']
		# If the user does not select a file, the browser submits an
		# empty file without a filename.
		if file.filename == '':
			print('No file name')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			print('Succes alumni')
			filename = secure_filename(file.filename)
			print(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		else:
			print('File name not allowed')
			return redirect(request.url)
		db.insert_alumni(nametext,desc,filename)

#######################################################
# team members form
#######################################################

	if "team-delete-form" in request.form:
		text = request.form['deleteteam']
		db.delete_team_members(text)
	if "team-add-form" in request.form:
		nametext = request.form['team-addname']
		desc = request.form['team-desc']
		role = request.form['role-desc']
		# check if the post request has the file part
		if 'team-file' not in request.files:
			print('No file part')
			return redirect(request.url)
		file = request.files['team-file']
		# If the user does not select a file, the browser submits an
		# empty file without a filename.
		if file.filename == '':
			print('No file name')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			print('Success team member')
			filename = secure_filename(file.filename)
			print(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		else:
			print('File name not allowed')
			return redirect(request.url)
		db.insert_team_members(nametext,desc,filename,role)

#######################################################
# Officer form
#######################################################

	if "officers-delete-form" in request.form:
		text = request.form['deleteofficers']
		db.delete_about(text)
	if "officers-add-form" in request.form:
		nametext = request.form['officers-addname']
		desc = request.form['officers-desc']
		# check if the post request has the file part
		if 'officers-file' not in request.files:
			print('No file part')
			return redirect(request.url)
		file = request.files['officers-file']
		# If the user does not select a file, the browser submits an
		# empty file without a filename.
		if file.filename == '':
			print('No file name')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			print('Success officer')
			filename = secure_filename(file.filename)
			print(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		else:
			print('File name not allowed')
			return redirect(request.url)
		db.insert_about(nametext,desc,filename)

#######################################################
# testimonial
#######################################################

	if "testimonial-delete-form" in request.form:
		text = request.form['deletetestimonial']
		db.delete_testimonial(text)
	if "testimonial-add-form" in request.form:
		nametext = request.form['testimonial-addname']
		desc = request.form['testimonial-desc']
		# check if the post request has the file part
		if 'testimonial-file' not in request.files:
			print('No file part')
			return redirect(request.url)
		filetext = request.files['testimonial-file']
		# If the user does not select a file, the browser submits an
		# empty file without a filename.
		if filetext.file == '':
			print('No file name')
			return redirect(request.url)
		if filetext and allowed_file(filetext.file):
			print('Success testimonial')
			file = secure_filename(filetext.file)
			print(os.path.join(app.config['UPLOAD_FOLDER'], file))
			filetext.save(os.path.join(app.config['UPLOAD_FOLDER'], file))
		else:
			print('File name not allowed')
			return redirect(request.url)
		db.insert_testimonial(nametext,desc,file)
		
	return render_template("admin.html", players=db.get_players())

@app.route('/logout')
def logout():
	flask_login.logout_user()
	return redirect('/')

@app.route('/sql_debug')
def sql_debug():
	return render_template("sql_debug.html", players=db.get_players())

# checks if file with filename is allowed to be uploaded
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

import flask
import flask_login
import os
from flask import Flask, flash, render_template, current_app, request, redirect, session
from flask_mail import Mail, Message
from werkzeug.utils import secure_filename
import google_calendar_reader as cal
import database_library as db
import pyotp
import datetime
import hashlib
from random import randrange


app = flask.Flask(__name__)
app.secret_key = os.urandom(16).hex() # Random 16 character string

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

# Our mock databases.
# irl we should use an actual database for this.
# We would also obviously not want to store username/login info in plain text like this.
users = {'foo@bar.tld': {'pw': 'secret'}, #for old login setup [Remove]
		 '08efdf7f9d382f19802a6ccb1a39c7531be4b1e5aaebdc2a49395ee656df22ab': {'pw': ''}, #testing personal gmail hash, use https://tools.keycdn.com/sha256-online-generator and insert email
		 '633f1794c55003374a30f8c046ed3022bae38f9ec9da834ce09c2e51b2e35e00': {'pw': ''}, #Club CSUS Email Hash
		 'c875fee06a22feda7227845dcd9680c34efd134d8d51fff72baffc08ba5bdeb5': {'pw': ''}} #Club Gmail Hash



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

#PyOTP TOTP instance
validation_interval_min = 3
secret =  pyotp.random_base32()
totp = pyotp.TOTP(secret, interval = (60 * validation_interval_min))


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

#used to time out session token after a set ammount of time of inactivity
time_out_interval = 10;
@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = datetime.timedelta(minutes=time_out_interval)

@app.route("/")
def welcome():
    newEvents = cal.get_next_five_events()
    #newEvents=[]
    return render_template("welcome.html",next_events=newEvents,block=db.get_page("homepage_about"),
			   joinusLink=db.get_link("joinusform"),donateLink=db.get_link("donate"),
			   social=db.get_page("social"))


@app.route("/donate")
def donate():
    return render_template("donate.html", donateLink=db.get_link("donate"), donateAffiliateLink = db.get_link("donateaff"),
			   social=db.get_page("social"), additional_donate_block=db.get_page("additional_info_donate"),
			   makedonation=db.get_page("make_a_donation"))

@app.route("/members")
def members():
    return render_template("members.html", member=db.get_team_members(),joinusLink=db.get_link("joinusform"),
	social=db.get_page("social"))

@app.route("/alumni")
def alumni():
	print(db.get_alumni())
	return render_template("alumni.html", alumni=db.get_alumni(), 
			block1=db.get_page("alumni1"),block2=db.get_page("alumni2"),
			mailingFormLink = db.get_link("mailingform"),
			social=db.get_page("social"))

@app.route("/calendar")
def calendar():
	oldEvents = cal.get_last_five_events()[:4]
	newEvents = cal.get_next_five_events()[:4]
	return render_template("calendar.html",past_events = oldEvents,next_events = newEvents,social=db.get_page("social"))

@app.route("/instagram")
def instagram():
    return render_template("instagram.html",
			   instagramLink = db.get_link("instagram"), flickrLink = db.get_link("flickr"),social=db.get_page("social"))

@app.route("/about")
def about():
    return render_template("about_us.html", officers=db.get_about(), content=db.get_page("aboutus"), 
			   joinusLink=db.get_link("joinusform"),social=db.get_page("social"))

#recruitment page
@app.route("/join")
def join():
    test = db.get_testimonial()
    
    return render_template("join.html",test=test,
			   block1=db.get_page("join_block1"),block2=db.get_page("join_block2"),block3=db.get_page("join_block3"),
			   joinusLink = db.get_link("joinusform"),social=db.get_page("social"))

@app.route("/contact")
def contact():
    return render_template("contactus.html",social=db.get_page("social"),logo=db.get_page("contact_logo"),
			   mailingFormLink = db.get_link("mailingform"))


@app.route("/contact",methods=['POST'])
def contact_post():
	msg = Message(subject=request.form['subject'],
				body="Hello, \n\n My name is "+request.form['name']+". My email is " + request.form['email']+ 
                        "\n\nHere is my message: "+request.form['message']+"\n\nYou can contact me at: "+request.form['phone']
                                    + "\n\n(Note: There is a message from Contact Page - Sac State Rowing Website)",
                        
				sender=request.form['email'],
				recipients=[emailAddress.rstrip()])
	mail.send(msg)
	return render_template("contactus.html",logo=db.get_page("contact"),social=db.get_page("social"))

@app.route("/recruitment")
def recruitment():
    return render_template("recruitment.html")
 
#Remove before transfering to client
@app.route('/login')
def login():
    return render_template("login.html",social=db.get_page("social"))

#Remove before transfering to client
@app.route('/login', methods=['POST'])
def login_form():
	email = flask.request.form['email']
	if flask.request.form['pw'] == users[email]['pw']:
		user = User()
		user.id = email
		flask_login.login_user(user)
		return flask.redirect(flask.url_for('protected'))
	return 'Bad login'

@app.route('/login_otp')
def login_otp():
	return render_template('login_otp.html', social=db.get_page("social") )

@app.route('/verify', methods = ["POST"])
def verify():
	#Generates OTP with PyOTP global var
	generated_otp = totp.now()
	#translates user inputed email to a hash value
	email_hash = hashlib.sha256(bytes(str(request.form['email_otp']), 'utf-8')).hexdigest()
	#Validate if email entered is in the system and
	#assigns the OTP to the email as its key value pair if email is in dictionary
	try:
		users[email_hash]['pw'] = str(generated_otp)
	except KeyError:
		flash("Email entered is invalid. Please try again")
		return render_template('login_otp.html', social=db.get_page("social") )
	#Sends message to email put in form
	msg = Message(subject="Rowing Club Sign-in Passcode",
				  body="Passcode for log-in verification: "
				  + str(generated_otp) + "\nPasscode will expire in " + str(validation_interval_min) + " minute(s).",  
				  sender="noreply@rowingclub.com", #curr ver shows sender same as recipient in actal email, see if there is a fix for this
				  recipients=[request.form['email_otp']])
	mail.send(msg)
	#Sets a session var to be referenced for validate page to test if code has expired. 
	session['generated_otp'] = generated_otp
	#Session var to generate log-in token for Flask Login
	session['email'] = email_hash
	return render_template('login_otp_validate.html', social=db.get_page("social") ) 


@app.route('/validate',methods=["POST"])
def validate():
	# OTP Entered by the User
	user_otp = request.form['otp'] 
	if totp.verify(otp=str(user_otp)):
		#validates user with Flask Login and generates Log-in token
		user = User()
		user.id = str(session['email'])
		flask_login.login_user(user, duration=datetime.timedelta(minutes=time_out_interval))
		return flask.redirect(flask.url_for('protected'))
	else:
		#checks whether the entered OTP is incorrect or if the Passcode has expired
		if totp.verify(session['generated_otp']):
			flash('Incorrect Passcode Entered, Try again')
			return render_template('login_otp_validate.html')
		else:
			flash('Passcode has timed out. Redirected to Login page.', social=db.get_page("social") )
			return render_template('login_otp.html', social=db.get_page("social") )


def file_allowed_handler(file):
	fname_prefix = file.filename.split(".")[0]
	fname_suffix = file.filename.split(".")[1]
	fname = ""
	fname = fname_prefix
	fname += str(randrange(1000000))+"_"
	fname += "{:%Y_%m_%d_%X}".format(datetime.datetime.now())
	fname += "."
	fname += fname_suffix
	file.filename = fname
	print(file.filename)
	filename = secure_filename(file.filename)
	print(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	return filename
	
@app.route('/protected', methods=['POST'])
@flask_login.login_required
def protected_post():
	print(request.form)
	if "deleteplayer" in request.form:
		text = request.form['deleteplayer']
		db.delete_player(text)
	if "player-name" in request.form:
		nametext = request.form['player-name']
		desc = request.form['player-desc']
		# check if the post request has the file part
		if 'player-file' not in request.files:
			print('No file part')
			return redirect(request.url)
		file = request.files['player-file']
		# If the user does not select a file, the browser submits an
		# empty file without a filename.
		if file.filename == '':
			print('No file name')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			print('Success')
			filename = file_allowed_handler(file)
		else:
			print('File name not allowed')
			return redirect(request.url)
		db.insert_player(nametext,desc,filename)
            
#######################################################
# Alumni form -> needs to be changed to edit text. Alumni memebers not a part of page
#######################################################

	if "deletealumni" in request.form:
		text = request.form['deletealumni']
		db.delete_alumni(text)
	if "alumni-name" in request.form:
		nametext = request.form['alumni-name']
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
			print('Success alumni')
			filename = file_allowed_handler(file)
		else:
			print('File name not allowed')
			return redirect(request.url)
		db.insert_alumni(nametext,desc,filename)

#######################################################
# team members form
#######################################################

	if "deleteteam" in request.form:
		text = request.form['deleteteam']
		db.delete_team_members(text)
	if "team-name" in request.form:
		nametext = request.form['team-name']
		desc = request.form['team-player-desc']
		role = request.form['team-role-desc']
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
			filename = file_allowed_handler(file)
		else:
			print('File name not allowed')
			return redirect(request.url)
		db.insert_team_members(nametext,desc,filename,role)

#######################################################
# Officer form
#######################################################

	if "deleteofficers" in request.form:
		text = request.form['deleteofficers']
		db.delete_about(text)
	#if "officers-add-form" in request.form:
	if "officers-name" in request.form:
		print('Officers add form')
		nametext = request.form['officers-name']
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
			filename = file_allowed_handler(file)
		else:
			print('File name not allowed')
			return redirect(request.url)
		db.insert_about(nametext,desc,filename)
#######################################################
# Testimonials form
#######################################################
	if "deletetestimonial" in request.form:
		text = request.form['deletetestimonial']
		db.delete_testimonial(text)
	if "testimonial-name" in request.form:
		nametext = request.form['testimonial-name']
		text1 = request.form['testimonial-text1']
		text2 = request.form['testimonial-text2']
		# check if the post request has the file part
		if 'testimonial-file' not in request.files:
			print('No file part')
			return redirect(request.url)
		file = request.files['testimonial-file']
		# If the user does not select a file, the browser submits an
		# empty file without a filename.
		if file.filename == '':
			print('No file name')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			print('Success testimonial')
			filename = file_allowed_handler(file)
		else:
			print('File name not allowed')
			return redirect(request.url)
		db.insert_testimonial(nametext,text1,filename,text2)

	team_members = db.get_team_members()
	#print(team_members)
	officers = db.get_about()
	#print(officers)
	testimonial=db.get_testimonial()
	#print(testimonial)
	return render_template("admin.html", 
							team_members=team_members, 
							officers=officers, 
							testimonial=testimonial,
              blocks=db.get_pages(),
			  links =db.get_links(),
			  social=db.get_page("social"))

@app.route('/protected')
@flask_login.login_required
def protected():
	team_members = db.get_team_members()
	#print(team_members)
	officers = db.get_about()
	#print(officers)
	testimonial=db.get_testimonial()
	#print(testimonial)
	return render_template("admin.html",
							team_members=team_members, 
							officers=officers, 
							testimonial=testimonial,
              blocks=db.get_pages(),
			  links =db.get_links(),
			  social=db.get_page("social"))

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

@app.route('/updatecontent', methods=['POST'])
@flask_login.login_required
def cmsPages():
	if flask.request.method == 'POST':
		json_data = flask.request.get_json()
		db.update_page(json_data["id"],json_data["content"])
		return {
			'data' : db.get_page(json_data["id"]),
			'message': "Updated Content!"
		}


@app.route('/editpage', methods=['POST'])
@flask_login.login_required
def updatePage():
	if flask.request.method == 'POST':
		json_data = flask.request.get_json()
		return {
			'data' : db.get_page(json_data["id"])
		}

@app.route('/uploadimage', methods=['POST'])
@flask_login.login_required
def uploadImage():
	if flask.request.method == 'POST':
		if request.files.get("file"):
			if allowed_file(request.files.get("file").filename):
				file = secure_filename(request.files.get("file").filename)
				request.files.get("file").save(os.path.join(app.config['UPLOAD_FOLDER'], file))
	return {
			'location' : os.path.join(app.config['UPLOAD_FOLDER'], file)
		}

@app.route('/updatelinks', methods=['POST'])
@flask_login.login_required
def updateLinks():
	if flask.request.method == 'POST':
		json_data = flask.request.get_json()
		for object in json_data["data"]:
			db.update_link(object,json_data["data"][object])
		return {
			'data' : db.get_links(),
			'message': "Saved Changes"
		}



          
	
            

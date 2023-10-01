import flask
import flask_login
import os
from flask import Flask, render_template, current_app, request, redirect
from flask_mail import Mail, Message
from werkzeug.utils import secure_filename
import google_calendar_reader as cal
import database_library as db

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

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/members")
def members():
    test = db.get_team_members
    return render_template("members.html", test=test)

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
 

@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
    	return render_template("login.html")
    email = flask.request.form['email']
    if flask.request.form['pw'] == users[email]['pw']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return flask.redirect(flask.url_for('protected'))
    return 'Bad login'

@app.route('/protected', methods=['POST'])
@flask_login.login_required
def my_form_post():
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
# sample copy of a secondary add form
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
	return render_template("admin.html", players=db.get_players(), alumni=db.get_alumni())

#######################################################
# testimonial
#######################################################
@app.route('/protected')
@flask_login.login_required
def protected():
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
	return render_template("admin.html", players=db.get_players(), testimonial=db.get_testimonial())

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

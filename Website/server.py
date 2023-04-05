import flask
import flask_login
from flask import Flask, render_template, current_app, request, redirect
import google_calendar_reader as cal

app = flask.Flask(__name__)
app.secret_key = 'super secret string'  # Change this!

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

# Our mock databases.
# irl we should use an actual database for this.
# We would also obviously not want to store username/login info in plain text like this.
users = {'foo@bar.tld': {'pw': 'secret'}} #for user login info
players = [('player1','Hello, my name is player1'),('player2','Hello, my name is player2'),('player3','Hello, my name is player3'),('player4','Hello, my name is player4'),('player5','Hello, my name is player5'),('player6','Hello, my name is player6')] #for templates

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
    return render_template("welcome.html", players=players)

@app.route("/contact")
def contact():
    return render_template("contact.html")
 
@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/members")
def members():
    return render_template("members.html")

@app.route("/calendar")
def calendar():
	oldEvents = cal.get_last_five_events()
	newEvents = cal.get_next_five_events()
	return render_template("calendar.html",past_events = oldEvents,next_events = newEvents)
	#return render_template("calendar.html",past_events = [],next_events = [])

@app.route("/instagram")
def instagram():
    return render_template("instagram.html")

#recruitment page
@app.route("/join")
def join():
    return render_template("recruitment.html")
 

@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
    	return render_template("login.html", players=players)
        #return '''
        #       <form action='login' method='POST'>
        #        <input type='text' name='email' id='email' placeholder='email'></input>
        #        <input type='password' name='pw' id='pw' placeholder='password'></input>
        #        <input type='submit' name='submit'></input>
        #       </form>
        #       '''

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
		for tup in players:
			if tup[0] == text:
				players.remove(tup) 
	if "add-form" in request.form:
		nametext = request.form['addname']
		desc = request.form['desc']
		players.append((nametext,desc))
	#return redirect('/')
	return render_template("admin.html", players=players)

@app.route('/protected')
@flask_login.login_required
def protected():
	#return current_app.send_static_file('admin.html')
	return render_template("admin.html", players=players)


@app.route('/logout')
def logout():
	flask_login.logout_user()
	#return 'Logged out'
	return redirect('/')
	return render_template("admin.html", players=players)

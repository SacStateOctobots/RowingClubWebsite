import flask
from flask import Flask, render_template, request

app = Flask(__name__) 

# This variable stores the value to be passed to the welcome.html template
sometext = "Hello world"

# When a user presses the submit button, the value in the corresponding text box for the form is retrieved,
# then that value is used to rebuild the welcome.html template and the built webpage is sent to them
@app.route("/", methods=['POST'])
def submit_input():
	text = request.form['sometext']
	sometext = text
	return render_template("welcome.html", sometext=sometext)

# When a user navigates to yourserverurl.com the template for welcome.html is built with the value of sometext and sent to them.
@app.route("/")
def display_page():
	return render_template("welcome.html", sometext=sometext)

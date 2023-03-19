import json
import urllib.request
import datetime
from dateutil.parser import *
from dateutil.rrule import *

# load api key from file
keyFile = open("API_KEY", "r")
key = keyFile.read()
keyFile.close()

# get data from google api
url = "https://www.googleapis.com/calendar/v3/calendars/c5fe0447d1a0e4d944df3016fb3743627f21dbccacf4f4b8c38c145effbc6e83@group.calendar.google.com/events?key="+key
f = urllib.request.urlopen(url)

# convert output json data to a python dictionary
out = json.loads(f.read())

# print output data
for a in out["items"]:
	print("Event:")
	if "summary" in a.keys():
		print("Summary: "+a["summary"])	
	if "description" in a.keys():
		print("Description: "+a["description"])	
	if "location" in a.keys():
		print("Location: "+a["location"])	
	print("Date time: "+a["start"]["dateTime"])	# this should be the date time of the very first occurrence I think
	if "recurrence" in a.keys():
		now = datetime.datetime.now()
		print("Recurrence rule: "+a["recurrence"][0])
		print("Next date time: "+str(rrulestr(a["recurrence"][0]).after(now)))
	print("")

import json
import urllib.request

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
#print(out) # this will print ALL the calendar output
for a in out["items"]:
	print("Event:")
	if "summary" in a.keys():
		print("Summary: "+a["summary"])	
	if "description" in a.keys():
		print("Description: "+a["description"])	
	if "location" in a.keys():
		print("Location: "+a["location"])	
	print("Date Time: "+a["start"]["dateTime"])	
	print("")

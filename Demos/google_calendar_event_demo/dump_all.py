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
print(out) # this will print ALL the calendar output

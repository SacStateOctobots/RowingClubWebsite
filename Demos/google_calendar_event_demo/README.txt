- The code in demo.py requests our calendar info via an http get request. The data it receives is one big json string so it next converts that into a big dictionary. After that it outputs some of the data.
- You will need an api key stored in a file named API_KEY to run this demo.

- the legit official way to use google calendar api is here: https://developers.google.com/calendar/api/quickstart/python
- A short wget hack to grab calendar info at the command line is: wget https://www.googleapis.com/calendar/v3/calendars/c5fe0447d1a0e4d944df3016fb3743627f21dbccacf4f4b8c38c145effbc6e83@group.calendar.google.com/events?key=<YOUR API KEY GOES HERE>

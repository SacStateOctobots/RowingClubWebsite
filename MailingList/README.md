"RemovingEntries.gs": Used as add on to the Google Sheets document linked to both forms in order to remove entries added from the Mailing list form based on responces from the Remove Email form.
This code must also have a timer set to run code for every form submission

"DeleteResponces.gs": Code te delete all responces to the form. This will not remove entries added to the Google Sheets document.
This code must also have a timer set to run code periodicly, currently timer is set to daily at midnight.

Note that when setting up Google app script code you must provide authorization from the google account that is using the script code. The rowing club must authorize changed being made by the code with their associated Google account when ownership is transfered.
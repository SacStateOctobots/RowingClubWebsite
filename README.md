# Rowing Club Website Read Me
## Project Summary

<img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rLogo.png" width="500">
The Rowing Club needs an updated website that can serve as a central hub for sharing information, connecting with members, and recruiting new members. This project is building a new website to fill this need.
<img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rHomepage.gif" width="500">


## Built with
* Python 3
* Flask
* SQLite 3
* HTML
* Javascript
* CSS+Bootstrap
* Jquery

## Testing
* Contact Us Email:

  - Navigate to contact us page.
  - Fill out contact us form and click submit.
  - Verify email submission is received in the email account setup in dev instructions section.

* Google Calendar Website Event Cards:

  - Verify landing page loads.
  - Verify cards at bottom of screen for landing page load with event data.
  - Verify event data consists of the four most recent events from the google calendar linked in setup from dev instructions.
  - Repeat the above steps on the calendar page.

 *  Animation On Scroll:
  - On landing page, about us page, contact us page and join page, verify page elements slide in/out of view while scrolling from top to bottom of page and back.

* Responsive Feature on Mobile Devices

* Login Function:
  - Navigate to <SITE URL>/login, enter admin login+password.
  - Make changes to data in admin panel.
  - Verify changes made in admin panel are updated on their corresponding site pages.


## How to Use (Deployment)
  - To run the website locally:
  - Under /Website use
  - `make`
  - Which runs the following command:
  - `flask --app server run`
  - This command starts an http server on your local machine on port 5000.
  - To access the site, navigate to http://localhost:5000 in your web browser.

# Dev Instructions
* Install SQLite3
* Use the package manager pip to install flask and modules (must have python3.7 or newer installed first):
  - pip install flask
  - pip install flask_login
  - pip install flask_mail
  - pip install  python-dateutil
  - npm install sass
* Note: Run setup_database.py script before running website to setup sqlite3 database file




### Enable Google App Passwords for SMTP (Contact page):
* First, Google App Passwords can only be used with accounts that have 2-Step Verification turned on.
* Open Google Account Security settings. Select App Passwords option.
  <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rGoggle1.png" width="500">
* Now, it is ready to set-up App Password…
* Create App Password
  - Click on Select App filed, choose Other (custom name) option:
  
  <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rGoogle2.png" width="400">
  
  - Enter an easily recognizable name, for example “Sac  State Rowing ”, and click Generate button
  
  <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rGoogle3.png" width="400">
  
  - From now on, always use this 16-character password (without spaces) and full Gmail address.
  
  <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rGoogle4.png" width="400">
  
  - Use this app password for API_KEY file and Email address for EMAIL ADDRESS file.
  
  <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rGoogle5.png" width="400">
  
### Google Calendar API (For Calendar page)
* Access to Google Developer Console
  
   <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rAPI1.png" width="400">
  
* Select Create Project
  
    <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rAPI2.png" width="400">
  
* Create Project name and Location (optional), then click Create
  
    <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rAPI3.png" width="400">
  
* After creating new project, Searching Google Calendar API and Enable
  
    <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rAPI4.png" width="400">
  
* After “Enable” Google Calendar API, from the left side, choose Credential and Select Create Credentials.
  
    <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rAPI5.png" width="400">
  
* We have an API key, but it is in “unrestricted mode.” To change it into “restricted mode,” click API key 1
  
    <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rAPI6.png" width="400">
    
    <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rAPI7.png" width="400">
  
* Lastly, copy API key and use it for API_Key file in Github
  
    <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rAPI8.png" width="400">
    
    <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rAPI9.png" width="400">
  
  
## Mock-up Diagrams
* Sitemap
  
  <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rSitemap.png" width="400">
  
* Flowchart
  
  <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rFlowchart.png" width="400">
  
## Project Features
* Landing Page:
  - Animated background.
  - Responsive animated page elements.
  - Access to rowing club recruitment form.
   
  <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rRecruitment.png" width="400">
  
  - Brief display of upcoming events via event cards.
 
  <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rEvenCard.png" width="400">
  

* Gallery Page:
  - Provides link to third party image hosting resource for rowing club event photos.

* Calendar Page:
  - Display of upcoming and past events via event cards.
  
  <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rUpcomingEvent.png" width="400">
  
  - Embedded calendar provides an in-depth view of all past and present events.
  
    <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rCalendar.png" width="400">
  
  - All events are modifiable by club members via access to a shared google calendar.

* Team Members Page:
  - Display of active team members via team member cards.
  
   <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rTeamMemberCard.png" width="400">
  
  - Team member cards will be modifiable through the admin page to keep the list of members up to date.
  - Links to alumni association page.
  
  <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rAlumni.png" width="400">

* Alumni Page:

* Login/Admin Page:
  - Not public facing.
  - Login page provides secure login to admin page. 
  
   <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rLogin.png" width="400">
  
  - Admin page allows for modification of site data by users.

* About Us Page:
  - Contains responsive animated page elements.
  - Displays a brief description of the rowing club.
  
  <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rBriefDes.png" width="400">
  
  - Includes cards displaying club officers.
  - Club officer cards and club information will be modifiable thru admin page.
  
    <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rClubOfficer.png" width="400">
  

* Social Media Page:
  - Contains an embedded instagram feed showing rowing club instagram posts.
  
  <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rSocial1.png" width="400">
  
  - Contains links to various rowing club social media accounts.
  
   <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rSocial2.png" width="400">

* Contact Page:
   - Links to rowing club social media.

  <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rContact1.png" width="400">
  
  - Includes video background.
  - Includes responsive animated page elements.
  - Contains various other club related contact info.
  - Includes “Contact Us” form which sends emails containing contact info from site users to a rowing club email for potential club members to inquire about the club.	

    <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rContact2.png" width="400">
  
  - Contains embedded map showing club location.
  
    <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rContact3.png" width="400">

* Join Page:
  - Also contains video background and responsive page elements.
  - Links to rowing club recruitment form.
  
    <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rJoin1.png" width="400">
  
  - Provides information to users interesting in joining the rowing club.
  
  <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rJoin2.png" width="400">

## Project Timeline (So Far)
### Sprint 01
* Research and barebones
* Getting an idea of what the client wants
* Putting together an initial tech stack (flask, bootstrap)
* Familiarizing team with tools for development

### Sprint 02
* First mockup of what the site looks like
* Layout for all of the pages
* Initial client feedback for the design of the website

### Sprint 03
* Clean up and standardize the look of the website
* Implement Client feedback
* Implementing integration of external API’s (Calendar, Instagram)
* Implemented UI and navigation
* Added animation to join page

### Sprint 04
* More client feedback! (Tweaks)
* Spike for backend in preparation for next semester
* Begin implementation of mailing list and login
* Added animation to additional site pages
* Project Timeline (Future)

### Sprint 05
* Start work on backend and backend dependent features (database, mailing list).
  
  <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rSprint5.png" width="400">

### Sprint 06
* Expand capabilities of admin user
  
    <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rSprint6.png" width="400">

### Sprint 07
* Final cleanup, standardization of desktop and mobile display
  
    <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rSprint7.png" width="400">

### Sprint 08
* Held in reserve for client feedback and timeline delay
  
    <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rSprint8.png" width="400">


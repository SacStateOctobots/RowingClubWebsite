# Rowing Club Website Read Me
  
  <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rLogo.png" width="500">

## Project Summary

  The OctoBots team was contracted by the Sacramento State Rowing Club to build an updated club website. The Rowing Club needed a website that can serve as a central hub for sharing information, connecting with members, and recruiting new members. This project is building a new website to fill these needs.
  
  <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rHomepage.gif" width="500">



## Table of Contents
- [Tools](#tools)
- [How To Use](#how-to-use)
- [Dev Instructions](#dev-instructions)
    - [Google App Passwords for SMTP Set-up](#enable-google-app-passwords-for-smtp-contact-page)
    - [Google Calendar API Set-up](#google-calendar-api-for-calendar-page)
- [Testing](#testing)
- [Mock-up Diagrams](#mock-up-diagrams)
- [Project Features](#project-features)
- [Project Timeline](#project-timeline)
    - [Spring 2023](#spring-2023)
    - [Fall 2023](#fall-2023)
- [AMI Setup](#ami-setup)

## Tools
* Python 3
* Flask
* SQLite 3
* HTML
* Javascript
* CSS+Bootstrap
* Jquery


## How to Use
  To run the website locally:
  Under /Website use
  
    make
  
  Which runs the following command:

    flask --app server run

  This command starts an http server on your local machine on port 5000.
  To access the site, navigate to http://localhost:5000 in your web browser.

## Dev Instructions
* Install SQLite3
* Use the package manager pip to install flask and modules (must have python3.7 or newer installed first):
  - `pip install flask`
  - `pip install flask_login`
  - `pip install flask_mail`
  - `pip install  python-dateutil`
  - `npm install sass`
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


* Animation On Scroll:
    - On landing page, about us page, contact us page and join page, verify page elements slide in/out of view while scrolling from top to bottom of page and back.


* Responsive Feature on Mobile Devices
    - Feature not yet implemented


* Login Function:
  - Navigate to <SITE URL>/login, enter admin login+password.
  - Make changes to data in admin panel.
  - Verify changes made in admin panel are updated on their corresponding site pages.



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

## Project Timeline
 ### Spring 2023
  * Sprint 01
     - Research and barebones
     - Getting an idea of what the client wants
     - Putting together an initial tech stack (flask, bootstrap)
     - Familiarizing team with tools for development
 

  * Sprint 02
     - First mockup of what the site looks like
     - Layout for all of the pages
     - Initial client feedback for the design of the website
 

  * Sprint 03
     - Clean up and standardize the look of the website
     - Implement Client feedback
     - Implementing integration of external API’s (Calendar, Instagram)
     - Implemented UI and navigation
     - Added animation to join page


  * Sprint 04
     - More client feedback! (Tweaks)
     - Spike for backend in preparation for next semester
     - Begin implementation of mailing list and login
     - Added animation to additional site pages
     - Project Timeline (Future)

 ### Fall 2023
  * Sprint 05
     - Start work on backend and backend dependent features (database, mailing list).
  
         <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rSprint5.png" width="400">

  * Sprint 06
     - Expand capabilities of admin user
  
         <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rSprint6.png" width="400">

  * Sprint 07
     - Final cleanup, standardization of desktop and mobile display
  
         <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rSprint7.png" width="400">

  * Sprint 08
     - Held in reserve for client feedback and timeline delay
  
## AMI Setup
### Instructions for migrating website to a new amazon account.
  - Follow the below instructions for handoff/serving of the website to another amazon account.
### 1. Make an AMI instance from the currently running website.
  - From our own dev amazon accounts/machines.
  - Follow instructions here: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami-ebs.html   
  - In particular follow the "Create a Linux AMI from an instance" section.
### 2. Share the AMI with another amazon account.
  - From our own dev amazon accounts/machines.
  - Retrieve the account ID of the amazon account you wish to share the AMI with.
  - Follow the instructions here: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharingamis-explicit.html
### 3. Configure the AMI for use by the second account.
  - From user amazon accounts/machines.
  - Under the AMIs tab of the ec2 console select launch instance and select the shared rowing club AMI.
  - Under Key pair (login) section select create a new keypair.
    - On linux I use the following config.
      - key pair name: Pick any key name you want. 
      - Key pair type: RSA
      - Private key file format: .pem
      - Then select create key pair and verify the file is downloaded to your local machine.
  - Under network settings select the "Allow HTTPS traffic from the internet" and "Allow HTTP traffic from the internet".
    - Leave other settings here as their defaults.
  - Start the instance by selecting launch instance.
  - Verify ssh works as expected.
    - On linux with the above config I do the following:
      - In the instances section of the amazon ec2 console copy the public ipv4 address of the instance.
      - Navigate to the directory containing the pem file.
      - Run `chmod go= your_pem_file_here.pem` in order to set up the permissions of the pem file.
      - run `ssh -i your_pem_file_here.pem ubuntu@ipv4_address_of_instance_here` to connect.
      - Verify that you are connected to the remote server.
    - On windows this process will be different.
  - Verify the website is currently being served by the instance.
    - On any web browser navigate to the address httpss://ipv4_address_of_instance_here to connect.
    - HTTPS keys and domain names will not yet be set up so this may trigger an https warning in your local browser.
    - Navigate through any warnings that your browser serves and you ought to finally be able to see the page.
### 4. Finalize website server setup.
  - From user amazon accounts/machines.
  - Setup Elastic ip address:
    - Follow the instructions here to allocate an elastic IP: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html#using-instance-addressing-eips-allocating
    - Next associate the allocated elastic IP to your instance.
    - Follow the instructions here to associate the elastic IP with your instance: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html#using-instance-addressing-eips-associating
    - With the new IP reverify you can connect to the website in the browser and via ssh as described above.
  - Point your domain name to the new elastic IP:
    - Consult your domain name providers documentation.
    - With the new domain name reverify you can connect to the website in the browser and via ssh like above but using your domain name.
  - Set up server side config files:
    - Navigate to /home/ubuntu/RowingClubWebsite/Website:
      - ssh into your instance as described in previous steps.
      - Run the following command to navigate to the website code: cd /home/ubuntu/RowingClubWebsite/Website
      - For the files ./nginx_venv_gunicorn_scripts/gen_ca_https_key.sh and ./nginx_venv_gunicorn_scripts/website:
        - Run the command: `./domain_name_changer.sh`
        - Input your domain name.
        - This regenerates several config files.
      - For the file API_KEY:
        - Run the command: `echo "YOUR_GOOGLE_CALENDAR_API_KEY_HERE" > API_KEY`
        - With your google calenddar api key in place of YOUR_GOOGLE_CALENDAR_API_KEY_HERE.
        - This command overwrites the API_KEY file with a new file containing your google calendar api key.
        - See user manual entry on setting up a google calendar api key.
      - For the file EMAIL_ADDRESS:
        - Run the command: `echo "YOUR_EMAIL_HERE" > EMAIL_ADDRESS`
        - With the email address you have setup for smtp in place of YOUR_EMAIL_HERE.
        - This command overwrites the EMAIL_ADDRESS file with the email you intend to use for smtp.
        - See user manual entry on setting up smtp.
      - For the file /EMAIL_KEY:
        - Run the command: `echo "SMTP_KEY_HERE" > EMAIL_KEY`
        - With the email key you have setup for smtp in place of SMTP_KEY_HERE.
        - This command overwrites the EMAIL_KEY file with the email key you intend to use for smtp.
        - See user manual entry on setting up smtp.
### 5. Restart the configured server.
  - Run the command: `make teardown`
    - Troubleshooting make teardown:
      - You can try and rerun make teardown several times.
      - Waiting for several minutes then rerunning make deploy.
      - Running the commands listed in the Makefile file under the teardown section individually (omit any @ signs at the start of any commands).
      - If none of the above works, identify the failing command in make teardown and consult its corresponding documentation.
      - Note: Errors here may be spurious. Do not consider this part failed until after verifying later make deploy commands fail too.
  - Run the command: `make deploy`
    - Troubleshooting make deploy:
      - You can try to rerun make teardown, then rerun make deploy.
      - You can try to rerun make teardown, then rerun the individual commands in the Makefile under the deploy section.
      - You can try and rerun the individual commands in the teardown, then deploy section of the Makefile.
      - You can try waiting several minutes then attempting all/some of the above again.
      - If none of the above works, identify the failing command in make deploy and consult its corresponding documentation.
      - Note: Errors here may be spurious. If the website is served (with no https errors) and works as expected consider this to be a success.
  - When make deploy is ran: 
      - you will need to click q when the nginx and/or gunicorn status screens are shown.
      - When the gen_ca_https_key.sh script runs you may be prompted to install a new cert or to renew an existing cert. You should prefer to renew the existing cert if the existing cert is currently valid and for the correct domain name.
        - Note: The certifying authority (letsencrypt) may rate limit you if you request too many certs within a short timeframe.
  - Note that if you delete a file, misconfigure a file, or otherwise ruin your current instance, you can always create a new fresh instance from our shared AMI. Doing this will require starting these instructions over however.
  - Note that if your https keys expire you can rerun the above command to renew them.
### 6. Final test of running website.
  - Check each page on the website to verify it displays correctly and all links/functionality work as intended.
  - Note that in particular you should verify in your browser that you are connected to the website using https without errors. View your browsers documentation for information on how to do this.

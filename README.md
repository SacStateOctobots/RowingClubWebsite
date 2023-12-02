# Rowing Club Website Read Me
  
  <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/img/rLogo.png" width="500">

## Project Summary

  The OctoBots team was contracted by the Sacramento State Rowing Club to build an updated club website. The Rowing Club needed a website that can serve as a central hub for sharing information, connecting with members, and recruiting new members. This project is building a new website to fill these needs.
  
  <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_home.PNG" width="500">



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
  
  <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_sitemap.PNG" width="500">
  
  
## Project Features

* Navigation Bar

   - The Navigation bar is visible at the top of all pages of the website. Clicking on the Logo will redirect the user to the Homepage of the website.

      - Desktop version:
      
      <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_menu_pc.PNG" width="600">

      - Tablet/ Mobile version: 

      <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_menu_phone1.PNG" width="400">

      <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_menu_phone2.PNG" width="400">

* Social Media Links Footer
   - This Footer is located at the bottom of all pages of the website. Provides quick links to the clubs main social media pages. Clicking on any of the provided buttons will redirect the user to the corresponding social media page for the club. Current links go to Facebook, the Rowing Clubs Instagram, and YouTube.

      <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_footer.png" width="400">
   
* Homepage:

   - Video Introduction Block:
   Plays a video of the Rowing Club in action creating an eye catching first impression for the site and shows users what the club is like.

     <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_homepage_banner.png" width="400">
  
   - About Us Block: 
   Shows a brief description about the Sacramento State Rowing Club’s history and mission statement

     <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_homepage_about.png" width="400">
  
   - Interest Block: 
   Provides a quick link to the Join Page if they have interest in joining the team.
   Clicking the “Join Us” button, it will redirect the user to Join page.

     <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_homepage_interesting.png" width="400">
   
   - Upcoming Events Block: 
   Shows a list of the next four upcoming events for the club. This is based on events in the clubs Google Calendar.

     <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_homepage_event.png" width="400">

   - Contribute Block: 
   Provides the user with a quick link to the Donate page if they wish to contribute financially to the club.
   Clicking the Donate button, it will redirect the user to the Donate page.

      <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_homepage_contribute.png" width="400">


* Calendar Page: Display of upcoming and past events via event cards.

   - Upcoming Events Block: 
   Shows a list of the next four upcoming events for the club. This is based on events in the clubs Google Calendar.

      <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_cal_banner.PNG" width="400">

   - Full Calendar Block:
   Displays the clubs Google calendar, listing all events for the current month.

      <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_cal_fullcal.PNG" width="400">

   - Past Events Block:
   Shows a list of the last four pasted events for the club. This is based on events in the clubs Google Calendar.

      <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_cal_pastevents.PNG" width="400">

   - Notice: All events are modifiable by club members via access to a shared google calendar.

* Current Roster Page:

   - Team member Banner:

     <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_team_banner.PNG" width="400">

   - Team member Block:
   Shows team member cards that contain information about each current member of the team. Displayed items include a photo of the team member, name, description, and player’s position.

     <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_team_member.PNG" width="400">
  
   - Interested Block: 
   Provides user with a quick link to the Recruitment Form that can be filled out in order to join the club.
   Clicking the Join Us button will redirect user to the Recruitment Form (Google Form) (*).

     <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_homepage_interesting.png" width="400">
   
   - Notice: Team member cards will be modifiable through the admin page to keep the list of members up to date.

* Social Media Page:

   - Instagram Embed and Flickr Embed:
   Shows a preview of the clubs Instagram and Flickr page. 

     <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_social.PNG" width="600">
   
   - Notice: For Instagram, clicking on the embedded view will redirect the user to the Instagram account & clicking on one of the images will redirect the user to the Instagram post. For Flickr, clicking on the embedded view will redirect the user to the Flickr album.



* Alumni Page:

   - Alumni Banner: There is a slider with 2 (or more) photos that will be changed every 5 sec.

     <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_alumni_banner.PNG" width="400">

   - Alumni Block 1:
   A description about the Alumni Association alongside a photo of the alumni’s rowing team

     <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_alumni_about.PNG" width="400">
  
   - Join Mailing List and description Block: 
   Provides a  link to the Rowing Club Mailing List sign-up Form to receive updates about the club activities. Clicking the button will redirect the user to Sign-up Mailing list Form (Google Form) (*)

     <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_alumni_join.PNG" width="400">


* About Us Page:

   - About Us Banner:

     <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_about_banner.PNG" width="400">

   - About Us Block 1:
   A description about the accolades and history of the club alongside a group photo of the rowing team.

     <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_about_info.PNG" width="400">
  
   - Officer Block:
   A content block full of the rowing club officers. Editable as an admin in admin login page

     <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_about_officer.PNG" width="400">

   - Interested Block: 
   Provides user with a quick link to the Recruitment Form that can be filled out in order to join the club.
   Clicking the Join Us button will redirect user to the Recruitment Form (Google Form) (*).

     <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_homepage_interesting.png" width="400">
   
   - Notice: Officer cards will be modifiable through the admin page to keep the list of officers up to date.

* Contact Us Page:

   - Video Introduction Block:
   Presents an introduction video giving a glimpse of sample club activities.
   Clicking the Sign up button redirects the user to the Sign-up Mailing list Form (Google Form) (*)

     <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_contact_intro.PNG" width="400">

   - Contact Info Block:
   Provides site users with the clubs address, email, and phone number as methods of getting in contact with them.

     <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_contact_info.PNG" width="400">
  
   - Rowing Club Email Form Block:
   Can be filled and submitted by site users to send an email to the rowing club email address.
   Form prompts user for name, email address (for responses), phone number, email subject, and message


     <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_contact_form.PNG" width="400">

   - Club Location Map Block:
   Shows the location of the rowing club to site users via an interactive Google map.

     <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_contact_map.PNG" width="400">
   

* Join Page:

   - Video Introduction Block:
   Plays a video of the Rowing Club in action creating an eye catching first impression for the site and shows users what the club is like.
   Clicking the Click Here button will redirect the user to the Recruitment Form (Google Form) (*)

     <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_join_intro.PNG" width="400">

   - Why Us Block:
   Lists the reasons why site user should participate in the Team.

     <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_join_why.PNG" width="400">
  
   - Interested Block: 
   Offers user second link to the Recruitment Form.
   Clicking the Join Us button, it will jump to Recruitment Form (Google Form) (*).

     <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_join_like.PNG" width="400">

   - Testimonials Block: 
   Testimonials about what it is like being a part of the club, written or spoken by current or past members or associates of the club.

     <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_join_cmt.PNG" width="400">


* Contribute Page:

   - Video Introduction Block:
   Presenting and introduction video.
   Clicking the More Information button will redirect the user to the Contact Page if the user wants to learn more about the club before contributing.

     <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_donate_intro.PNG" width="400">

   - Contribution Block:
   The user is provided two different ways to support the Team.
   Clicking Donate button will redirect the user to Sac State Sport Club page (*).
   Below this is Rowing Club’s address where a user can send a check.

     <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_donate_btn.PNG" width="400">
  

* External Links:
  - [Sac State Rowing Club Recruitment Form](https://docs.google.com/forms/d/e/1FAIpQLSfZgOi84FUsV-uXBSIsJuTX3pKZdlFydBgsojzrhYNo09q4ZA/viewform)

  - [Rowing Club Mailing List Sign-up](https://docs.google.com/forms/d/e/1FAIpQLSe4fk45Z9j-oDdYpRmqj_QyHlHeVUtFmN9naGly7g6DEWgDOg/viewform)

  - [Sacramento State Sport Clubs](https://swarmfunding.csus.edu/project/36577/donate)


* Login OTP:
  - This page will be hidden to the user, and it will not show on the navigation bar (only show in testing mode). Login page is using the Email One-time Passcode (OTP) method. Users, in this case, administrator, must enter a valid email to which an OTP code will be sent. Entry of valid code will redirect to the Admin Page.
  
  - Notice: This page can be accessed by entering https://<Site Domain Name>/login_otp. 
  For example: (Example: https://octobotgroup.work/login_otp)

    - Step 1: Enter the admin email present in the website database. Entering an unassigned email will prompt the user to re-enter a valid email. Entering a valid email will redirect user to the validation page.

      <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_login_otp.PNG" width="400">
             
    - Step 2: Check entered email to get passcode for entry on next page. Passcode will expire in 3 minutes. 
      Notice: If users enter the email at step 1 that is different from database, they will have a notification such as "Email entered is invalid. Please re-enter your email."

      <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_login_step2.PNG" width="400">

    - Step 3: Enter passcode. If incorrect email or passcode is entered the page will reload and re-prompt the user for entry of credentials. If passcode has expired the page will redirect to the previous email entry page and warn the user that the passcode has expired re-prompting for email entry to send a new passcode.
      Once the process is successful, the page will redirect user to the Admin page.
      Notice: If users enter the email at step 3 that is different from received email, they will have a notification such as "Passcode entered is invalid. Please re-enter Passcode."

        <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_login_step3.PNG" width="400">


* Admin Portal:

  - General Admin page layout: This layout applies for Team Members, Officers, and Testimonial Tabs.

      <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_admin_general.png" width="600">

      - Selection Area [Red]: Listing all Team members, officers, and current Testimonials that are present on the site.

      - Tabs  [Blue]: Clicking on different tabs will show different prompts for section of the site that are editable. Tabs including Team Members, Officers, Testimonial, Content Blocks, and Social Links.

      - Deleting Section [Orange]: Dropdown lists all “items” on database for selected tab. Once clicking the Delete button, the item will be deleted from the database. Confirmation of deletion is reflected by the corresponding “item” being removed  from Selection Area. 

      - Adding Section [Green]: Form lists all information that the admin needs to enter to add a new “item.” Once clicking the Add button, the item will be added in database. Confirmation of this addition is reflected by the corresponding “item” appearing on the Selection Area.

      - Showing Section [Purple]: This section shows the “item” which is selected from Selection area. Displaying photo, name, position, etc. 



  - Selection Area: Item Selection
    - How to select and view information for an “item” from the Selection Area of the Admin Portal.
    - This applies for Team Member, Officers, and Testimonial tabs.
  
      <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_admin_selection.png" width="600">

      - Step 1: Select and “item” from the Selection Area. Image shows “Officer 3” under the Current Officers List is selected by admin.

      - Step 2: If not already on the related tab, admin will need to navigate to the corresponding tab to the selected “item”. Image shows Officer Tab is selected.

      - Step 3: All information of the selected “item” will be show in the Member Selected section. Image shows the information for “Officer 3”.



  - Deleting Section: Deleting an Item
    - How to delete an “item” that is present on the Selection Area of the Admin Portal so it will be removed from the database and no longer appear on the related site page.
    - This applies for Team Member, Officers, and Testimonial tabs.

      <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_admin_delete1.png" width="600">

      - Step 1:  Select the corresponding tab for the item the admin wants to delete. Example image shows the Officer Tab is selected.

      - Step 2: In the Deletion Section select the item the admin wants to delete from the dropdown menu. Then, click “Delete Officer” button to confirm selection.
      Example image shows “Officer 3” is selected from the dropdown list. 

      <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_admin_delete2.png" width="600">

      - Step 3: Confirmation of  “item” deletion can be seen in the  Selection Area. 
      Example image shows there is now 1 less officer and Officer 3 is no longer listed.



  - Adding Section: Adding an Item
    - How to add an “item” to the database so it will appear on the related site page and on the Selection Area of the Admin Portal.
    - This applies for Team Member, Officers, and Testimonial tabs.

      <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_admin_add1.png" width="600">

      - Step 1:  Select the corresponding tab for the item the admin wants to add. Example image shows the Officer Tab is selected.

      - Step 2: Fill out all information, such as name, officer's description, and photo. Then, click “Add Officer.”

      <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_admin_add2.png" width="600">

      - Step 3: Confirmation of  “item” creation can be seen in the  Selection Area. 
      The example image shows the new “John Doe” item and there are 3 officers instead of 4.

      - Step 4: Further confirmation of added item information can be seen in the Selection View section of the Admin Page. 
      Example image shows the additional information for the added “John Doe” item.


  - Content Block Tab: 
    - Content Blocks provide the admin ability to modify contents of the website, including text and photo from Admin Portal.

      <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_admin_content.png" width="600">

      - Step1: Select the Content Block tab.

      - Step 2: In the content block table click on the text from a cell under the Title column.
      Example image shows the About Us text selected. 

      - Step 3: Admin user can change the text and images in the text editor window for the selected Content Block section. 
      Example image shows the About Page text content and an image.

      <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_admin_content1.png" width="300">

      - Step 4: Should the admin want to change the image, right click the image and choose upload. When uploading new image, remove the value on width and height attributes then click save.

      - Step 5: When all changed have been made click the“Update Now” button.

      <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_admin_content2.png" width="500">

      - Step 6: Confirmation that the changes have been made by navigating to the associated site page and viewing the section that was changed.
      Example image shows changes made to the About page.


  - Social Links Tab:
    - The Social Media tab provides the admin ability to modify the links to off site pages on the website from the Admin Portal.

      <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_admin_social.png" width="500">

      - Step 1: Social Links is chosen.

      - Steep 2: Add/ Change links. Then “Save Changes” 


  - Google Calendar:
    - Instruction for accessing and adding an event to the google calendar for admin users.

      <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_admin_g1.png" width="500">

      - Step 1: Click on the google calendar icon on the bottom right of the calendar embed. 

      <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_admin_g2.png" width="500">

      - Step 2: Make sure only the appropriate calendar is selected in the My Calendars dropdown of your Google Calendar account

      - Step 3: Click on the desired time and date on the google calendar area to open the event edit menu.

      - Step 4: Make any adjustments to the event in the menu and click “Save” to add the event to the calendar.

  
  
    - Should the admin wish to alter the visibility or delete event blocks from calendar:
  
      <img src="https://github.com/SacStateOctobots/RowingClubWebsite/blob/main/Website/static/readmePhoto/rm_admin_g3.png" width="500">

      - Step: Double click on the event you wish to change and further edit or delete the event in the menu that opens.



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
     - Research Database Solutions and begin database implemenation
     - Register URL and get site hosted
     - Create Google Forms for mail list and club sign up

  * Sprint 06
     - Standardize UI and fix display errors
     - Setup scripts for testing and deployment
     - Create Alumni Page
     - Make UI compatible with mobile devices
     - Research 3rd party image hosting

  * Sprint 07
     - Standardization of desktop and mobile display
     - Change gallery page to donate page
     - Implement Admin page secure login
     - Admin Page visual overhall
     - Implement Admin page database access and site editability
     - Implement testing with Selenium

  * Sprint 08
     - Expand abilities of admin page to edit site
     - General site and admin page UI tweaks
     - Bug fixes
     - backend clean up
     - expand login process
  
  * Sprint 09
     - Increase security features of login process
     - implement client requested UI tweaks
     - Create procedures to restore site in case of incident
     - Social Media page tweaks
     - Implement admin page ability to change where site links direct to

  * Sprint 10
     - Code Clean Up and Finalization
     - Documentation for Client User and Maintenance Manuals
     - Product Delivery

  
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

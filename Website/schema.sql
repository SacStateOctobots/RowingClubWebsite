-- a sample sql table
CREATE TABLE IF NOT EXISTS players (
	name VARCHAR(255) NOT NULL UNIQUE, 
	description VARCHAR(255) NOT NULL, 
	imgfilename VARCHAR(255) NOT NULL);
-- some sample inputs
INSERT INTO players (name, description, imgfilename) VALUES ('Player1', 'Hello, my name is Player1.','Cat1.jpg');
INSERT INTO players (name, description, imgfilename) VALUES ('Player2', 'Hello, my name is Player2.','Cat2.jpg');
INSERT INTO players (name, description, imgfilename) VALUES ('Player3', 'Hello, my name is Player3.','Cat3.jpg');
INSERT INTO players (name, description, imgfilename) VALUES ('Player4', 'Hello, my name is Player4.','Cat4.jpg');
INSERT INTO players (name, description, imgfilename) VALUES ('Player5', 'Hello, my name is Player5.','Cat5.jpg');

CREATE TABLE IF NOT EXISTS testimonials (
	name VARCHAR(255) NOT NULL UNIQUE, 
	testimonial VARCHAR(255) NOT NULL, 
	imgfilename VARCHAR(255) NOT NULL,
	job VARCHAR(255) NOT NULL);

INSERT INTO testimonials (name, testimonial, imgfilename,job) VALUES ('Spiderman', 'A testimonial from a
                            client who benefited from your product or service.
                            Testimonials can be a highly effective way of establishing
                            credibility and increasing your companys reputation.','Spider-Man.jpg','superhero');
INSERT INTO testimonials (name, testimonial, imgfilename,job) VALUES ('Rambunctious Cat', 'A testimonial from a rambunctious cat. Probably hopped up on catnip.','Cat1.jpg','small cat');
INSERT INTO testimonials (name, testimonial, imgfilename,job) VALUES ('Annoyed Cat', 'A testimonial from a perturbed feline.','Cat2.jpg','smaller cat');




CREATE TABLE IF NOT EXISTS team_members (
    name VARCHAR(255) NOT NULL UNIQUE,
    description VARCHAR(255) NOT NULL,
    imgfilename VARCHAR(255) NOT NULL,
    role VARCHAR(255) NOT NULL);

-- Insert team member data
INSERT INTO team_members (name, description, imgfilename, role) VALUES
	('Team Member 1', 'Hello, I am Team Member 1.', 'Amaka Okam.jpg', 'Role 1'),
	('Team Member 2', 'Hello, I am Team Member 2.', 'Bryleigh Nixon.jpg', 'Role 2'),
    ('Team Member 3', 'Hello, I am Team Member 3.', 'Daria Okhremtchuk.jpg', 'Role 3'),
	('Team Member 4', 'Hello, I am Team Member 4.', 'Ella Holmes.jpg', 'Role 4'),
    ('Team Member 5', 'Hello, I am Team Member 5.', 'Harper Waring.jpg', 'Role 5');

CREATE TABLE IF NOT EXISTS alumni (
	name VARCHAR(255) NOT NULL UNIQUE, 
	description VARCHAR(255) NOT NULL, 
	imgfilename VARCHAR(255) NOT NULL);	

INSERT INTO alumni (name, description, imgfilename) VALUES ('Alumni1', 'Hello, my name is Alumni1.','Cat1.jpg');
INSERT INTO alumni (name, description, imgfilename) VALUES ('Alumni2', 'Hello, my name is Alumni2.','Cat2.jpg');	

-- sql table for officers (about page)
CREATE TABLE IF NOT EXISTS officers (
	name VARCHAR(255) NOT NULL UNIQUE,
	description VARCHAR(255) NOT NULL, 
	filename VARCHAR(255) NOT NULL);

INSERT INTO officers (name, description, filename) VALUES 
 ('Officer1', 'This is test text for officer1.', 'Kennedy Kolbeck.jpg'),
 ('Officer2', 'This is test text for officer2.', 'Manindar VerBrugge.jpg'),
 ('Officer3', 'This is test text for officer3.', 'Mike Connors.jpg'),
 ('Officer4', 'This is test text for officer4.', 'Sarah Puddicombe.jpg'),
 ('Officer5', 'This is test text for officer5.', 'Nieka Marais.jpg');


-- sql table for cmspages (about page)
CREATE TABLE IF NOT EXISTS cmspages (
	id VARCHAR(255) NOT NULL UNIQUE,
	title VARCHAR(255) NOT NULL UNIQUE, 
	content TEXT NOT NULL,
	modifieddate VARCHAR(255));

INSERT INTO cmspages (id, title, content, modifieddate) VALUES ('aboutus', 'About Us', 
"<div class='col-lg-6'><p style='font-size:22px' data-aos='fade-right' data-aos-duration='1000'>&#x2022; Since 1984 the Sacramento State Men's Rowing team has competed against universities from all over the country. As part of the Western Intercollegiate Rowing Association, the team has won multiple conference championships in the Varsity 8. They also have had championship boats in several other events during the team’s history.</p><p style='font-size:22px' data-aos='fade-left' data-aos-duration='1000'>&#x2022; The members of this team throughout history pride themselves on hard work, dedication, and commitment to a common goal. (Competition & Practice Schedules with be added soon) In 2021, the club transitioned to become the Rowing Club, now offering both men’s and women’s rowing.</p></div><div class='col-md-6' data-aos='fade-down' data-aos-duration='1000'><img class='img-fluid rounded w-100' src='./static/img/p5.jpeg'></div>",datetime('now'));
INSERT INTO cmspages (id, title, content, modifieddate) VALUES ('social', 'Social Block',
"<div class='wrapper-social-icon'><div class='button-social'><div class='social-icon'><em class='fab fa-facebook-f'>&nbsp;</em></div><a href='https://facebook.com'><span>Facebook</span></a></div><div class='button-social'><div class='social-icon'><em class='fab fa-instagram'>&nbsp;</em></div><a href='https://instagram.com'><span>Instagram</span></a></div><div class='button-social'><div class='social-icon'><em class='fab fa-youtube'>&nbsp;</em></div><a href='https://youtube.com'><span>YouTube</span></a></div></div>",datetime('now'));
INSERT INTO cmspages (id, title, content, modifieddate) VALUES ('contact', 'Contact Information',
"<p style='color:black'>Have any questions?</p><br><p style='color:black;'>Email us at abcd@csus.com</p>",datetime('now'));
INSERT INTO cmspages (id, title, content, modifieddate) VALUES ('contact_logo', 'Contact Logo',
"<div class='col-md-4' style='text-align:center'><div class='contact-icon' data-aos='fade-down' data-aos-duration='1000'><div class='icon'><i class='fas fa-home'></i></div><h3>VISIT US</h3><p>We always welcome you at</p><h4>1901 Hazel Ave,<br>Gold River, CA 95670</h4></div></div><div class='col-md-4' style='text-align:center'><div class='contact-icon' data-aos='fade-down' data-aos-duration='1000' data-aos-delay='300'><div class='icon'><i class='fas fa-phone'></i></div><h3>CALL US</h3><p>We are happy to hear from you</p><h4>+1 209 123 4567</h4></div></div><div class='col-md-4' style='text-align:center'><div class='contact-icon' data-aos='fade-down' data-aos-duration='1000' data-aos-delay='600'><div class='icon'><i class='fas fa-envelope'></i></div><h3>Email US</h3><p>Even you can send us any messages</p><h4>rowing@abcd.csus.edu</h4></div></div>",datetime('now'));
INSERT INTO cmspages (id, title, content, modifieddate) VALUES ('homepage_about', 'About Us on Homepage',
"<div class='container-xxl py-5'><div class='name-events'>About us</div><div class='name-phone'>About us</div></div><p data-aos='fade-down' data-aos-duration='1000'>Sacramento State Rowing Club exists to provide the development opportunity for collegiate rowers to make the step from university rowing to Senior National Team competition. Rowers from California State University, Sacramento and all across the U.S. are welcome to join the CRC to develop technically and physically with the goal of progressing into their respective national teams.<div class='space15'></div><p data-aos='fade-down' data-aos-duration='1000'>Besides, Sac State Rowing Club's website contains many of the ongoing events and current team member rosters and evrything Sacramento State Rowing related.<p data-aos='fade-down' data-aos-duration='1000'>Stingers up!</p>",datetime('now'));

INSERT INTO cmspages (id, title, content, modifieddate) VALUES ('alumni1', 'Alumni Page Block 1',
"<div class='col-lg-6'><p style='font-size:22px' data-aos='fade-right' data-aos-duration='1000'>&#x2022; This section will be a few paragraphs long and have info regarding what the Alumni Association is and what Alumni in general have been doing. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco.</p><p style='font-size:22px' data-aos='fade-left' data-aos-duration='1000'>&#x2022; This section will be a few paragraphs long and have info regarding what the Alumni Association is and what Alumni in general have been doing. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco.</p></div><div class='col-md-6' data-aos='fade-down' data-aos-duration='1000'><img class='img-fluid rounded w-100' src='./static/img/p5.jpeg'></div>",datetime('now'));
INSERT INTO cmspages (id, title, content, modifieddate) VALUES ('alumni2', 'Alumni Page Block 2',
"<div class='text-heading mx-auto'><h1>What Have Alumni Been Up To?</h1></div><div class='card text-left green_back_gold_front mx-auto'><div class='card-body'><p style='font-size:22px' data-aos='fade-right' data-aos-duration='1000'>This section will be a few paragraphs long and have info regarding what the Alumni Association is and what Alumni in general have been doing. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco.</p><p style='font-size:22px' data-aos='fade-left' data-aos-duration='1000'>This section will be a few paragraphs long and have info regarding what the Alumni Association is and what Alumni in general have been doing. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco.</p></div></div>",datetime('now'));

INSERT INTO cmspages (id, title, content, modifieddate) VALUES ('join_block1', 'Join Page - Block Why Us',
"<div class='col-lg-6'><div class='row g-3'><div class='col-6 text-end'><img class='img-fluid rounded w-75' data-aos='fade-down' data-aos-duration='1000' src='./static/img/p1.png' style='margin-top:0'></div><div class='col-6 text-start'><img class='img-fluid rounded w-100' data-aos='fade-left' data-aos-duration='1000' src='./static/img/p2.jpeg'></div><div class='col-6 text-end'><img class='img-fluid rounded w-130' data-aos='fade-right' data-aos-duration='1000' src='./static/img/p3.jpeg' style='margin-top:-60%'></div><div class='col-6 text-start'><img class='img-fluid rounded w-75' data-aos='fade-up' data-aos-duration='1000' src='./static/img/p4.jpeg'></div></div></div><div class='col-lg-6'><div class='text-heading' data-aos='fade-down' data-aos-duration='1000'><h1>Why us?</h1></div><p style='font-size:22px' data-aos='fade-up' data-aos-duration='1000'>&#x2022; Sac State rowing lets you meet new individuals and make new friends. The friendships that you develop will stay with you throughout your life. The learnings that you gain through practice can be applied in various ways, such as in the classroom and in the real world. The community also extends beyond the country, state, and city limits.</p></div>",datetime('now'));
INSERT INTO cmspages (id, title, content, modifieddate) VALUES ('join_block2', 'Join Page - Second Block',
"<div class='col-lg-6'><p style='font-size:22px' data-aos='fade-right' data-aos-duration='1000'>&#x2022; You’ll meet new people through the practice of rowing. The goal of the team is to build a close-knit environment where all members are dedicated to achieving success. We encourage a competitive environment and strive to improve the members’ performance.</p><p style='font-size:22px' data-aos='fade-left' data-aos-duration='1000'>&#x2022; The goal of the program is to provide a challenging environment that pushes the members' physical and mental limits. Through the program, you'll have the opportunity to travel across the country and compete against other club teams around the U.S.</p></div><div class='col-md-6'><img class='img-fluid rounded w-100' data-aos='fade-down' data-aos-easing='ease-out-cubic' data-aos-duration='1000' src='./static/img/p5.jpeg'></div>",datetime('now'));
INSERT INTO cmspages (id, title, content, modifieddate) VALUES ('join_block3', 'Join Page - Third Block',
"<div class='col-lg-6'><div class='text-heading'><h1 class='mb-4' data-aos='fade-right' data-aos-duration='1000'>Interested to Being a part of the Team?</h1></div><p style='text-align:center;font-size:22px' data-aos='zoom-in' data-aos-duration='1000'>All are welcome with<b>NO EXPERIENCE REQUIRED</b></p><div class='video-introduction-content-button'><a data-aos='fade-left' data-aos-duration='1000' href='https://docs.google.com/forms/d/e/1FAIpQLSfZgOi84FUsV-uXBSIsJuTX3pKZdlFydBgsojzrhYNo09q4ZA/formResponse'>Join us</a></div></div><div class='col-lg-6'><div class='row g-3'><div class='col-6 text-end'></div><div class='col-6 text-start'><img class='img-fluid rounded w-100' data-aos='zoom-in' data-aos-duration='1000' data-aos-delay='0' src='./static/img/p7.jpeg'></div><div class='col-6 text-end'><img class='img-fluid rounded w-100' data-aos='zoom-in' data-aos-duration='1000' data-aos-delay='200' src='./static/img/p8.jpeg' style='margin-top:-65%'></div><div class='col-6 text-start'><img class='img-fluid rounded w-75' data-aos='zoom-in' data-aos-duration='1000' data-aos-delay='400' src='./static/img/p6.jpeg'></div></div></div>",datetime('now'));

-- Table for OTP log-in email storage
-- not currently implemented for use
-- change to rowingclub email once site is ready for release
CREATE TABLE IF NOT EXISTS loginEmail (
	emailAddr VARCHAR(255) NOT NULL UNIQUE);
INSERT INTO loginEmail (emailAddr) VALUES ('lynnjess.dev@gmail.com')


--testimonials table and data
CREATE TABLE IF NOT EXISTS testimonials (
	name VARCHAR(255) NOT NULL UNIQUE, 
	testimonial VARCHAR(255) NOT NULL, 
	imgfilename VARCHAR(255) NOT NULL,
	job VARCHAR(255) NOT NULL);

INSERT INTO testimonials (name, testimonial, imgfilename,job) VALUES 
	('Spiderman', 'A testimonial from a
                            client who benefited from your product or service.
                            Testimonials can be a highly effective way of establishing
                            credibility and increasing your companys reputation.','Spider-Man.jpg','superhero'),
	('Rambunctious Cat', 'A testimonial from a rambunctious cat. Probably hopped up on catnip.','Cat1.jpg','small cat'),
	('Annoyed Cat', 'A testimonial from a perturbed feline.','Cat2.jpg','smaller cat');

--team members table and data
CREATE TABLE IF NOT EXISTS team_members (
    name VARCHAR(255) NOT NULL UNIQUE,
    description VARCHAR(255) NOT NULL,
    imgfilename VARCHAR(255) NOT NULL,
    role VARCHAR(255) NOT NULL);

INSERT INTO team_members (name, description, imgfilename, role) VALUES
	('Team Member 1', 'Hello, I am Team Member 1.', 'Amaka Okam.jpg', 'Role 1'),
	('Team Member 2', 'Hello, I am Team Member 2.', 'Bryleigh Nixon.jpg', 'Role 2'),
    ('Team Member 3', 'Hello, I am Team Member 3.', 'Daria Okhremtchuk.jpg', 'Role 3'),
	('Team Member 4', 'Hello, I am Team Member 4.', 'Ella Holmes.jpg', 'Role 4'),
    ('Team Member 5', 'Hello, I am Team Member 5.', 'Harper Waring.jpg', 'Role 5');	

--officers table and data (about page)
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

--cmspages table and data (about page)
CREATE TABLE IF NOT EXISTS cmspages (
	id VARCHAR(255) NOT NULL UNIQUE,
	title VARCHAR(255) NOT NULL UNIQUE, 
	content TEXT NOT NULL,
	modifieddate VARCHAR(255));

--various other content blocks
INSERT INTO cmspages (id, title, content, modifieddate) VALUES ('aboutus', 'About Us', 
"<div class='col-lg-6'><p style='font-size:22px' data-aos='fade-right' data-aos-duration='1000'>&#x2022; Since 1984 the Sacramento State Men's Rowing team has competed against universities from all over the country. As part of the Western Intercollegiate Rowing Association, the team has won multiple conference championships in the Varsity 8. They also have had championship boats in several other events during the team's history. The members of this team throughout history pride themselves on hard work, dedication, and commitment to a common goal. In 2021, the club transitioned to become the Rowing Club, now offering both men's and women's rowing.</p></div><div class='col-md-6' data-aos='fade-down' data-aos-duration='1000'><img class='img-fluid rounded w-100' src='./static/img/p5.jpeg'></div>",datetime('now'));
INSERT INTO cmspages (id, title, content, modifieddate) VALUES ('social', 'Social Block',
"<br/><p>Have any questions?</p><br/><p>Email us at so-rowingclub@csus.edu</p><div class='wrapper-social-icon'><div class='button-social' data-aos='fade-down' data-aos-duration='1000'><div class='social-icon'><i class='fab fa-facebook-f'>&nbsp;</i></div><a href='https://facebook.com'><span>Facebook</span></a></div><div class='button-social' data-aos='fade-up' data-aos-duration='1000' data-aos-delay='200'><div class='social-icon'><i class='fab fa-instagram'>&nbsp;</i></div><a href='https://instagram.com'><span>Instagram</span></a></div><div class='button-social' data-aos='fade-down' data-aos-duration='1000' data-aos-delay='400'><div class='social-icon'><i class='fab fa-youtube'>&nbsp;</i></div><a href='https://youtube.com'><span>YouTube</span></a></div><div class='space80'></div></div>",datetime('now'));
INSERT INTO cmspages (id, title, content, modifieddate) VALUES ('contact_logo', 'Contact Logo',
"<div class='col-md-4' style='text-align:center'><div class='contact-icon' data-aos='fade-down' data-aos-duration='1000'><div class='icon'><i class='fas fa-home'></i></div><h3>VISIT US</h3><p>We always welcome you at</p><h4>1901 Hazel Ave,<br>Gold River, CA 95670</h4></div></div><div class='col-md-4' style='text-align:center'><div class='contact-icon' data-aos='fade-down' data-aos-duration='1000' data-aos-delay='300'><div class='icon'><i class='fas fa-phone'></i></div><h3>CALL US</h3><p>We are happy to hear from you</p><h4>+1 916-278-6595</h4></div></div><div class='col-md-4' style='text-align:center'><div class='contact-icon' data-aos='fade-down' data-aos-duration='1000' data-aos-delay='600'><div class='icon'><i class='fas fa-envelope'></i></div><h3>Email US</h3><p>Even you can send us any messages</p><h4>so-rowingclub@csus.edu</h4></div></div>",datetime('now'));
INSERT INTO cmspages (id, title, content, modifieddate) VALUES ('homepage_about', 'About Us on Homepage',
"<div class='container-xxl py-5'><div class='name-events'>About us</div><div class='name-phone'>About us</div></div><p data-aos='fade-down' data-aos-duration='1000'>Since 1984 the Sacramento State Men's Rowing team has competed against universities from all over the country. As part of the Western Intercollegiate Rowing Association, the team has won multiple conference championships in the Varsity 8. They also have had championship boats in several other events during the team's history. The members of this team throughout history pride themselves on hard work, dedication, and commitment to a common goal. In 2021, the club transitioned to become the Rowing Club, now offering both men's and women's rowing.<p data-aos='fade-down' data-aos-duration='1000'></p>",datetime('now'));

--alumni content blocks
INSERT INTO cmspages (id, title, content, modifieddate) VALUES ('alumni1', 'Alumni Page Block 1',
"<div class='col-lg-6'><p style='font-size:22px' data-aos='fade-right' data-aos-duration='1000'>&#x2022; This section will be a few paragraphs long and have info regarding what the Alumni Association is and what Alumni in general have been doing. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco.</p><p style='font-size:22px' data-aos='fade-left' data-aos-duration='1000'>&#x2022; This section will be a few paragraphs long and have info regarding what the Alumni Association is and what Alumni in general have been doing. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco.</p></div><div class='col-md-6' data-aos='fade-down' data-aos-duration='1000'><img class='img-fluid rounded w-100' src='./static/img/p12.png'></div>",datetime('now'));
INSERT INTO cmspages (id, title, content, modifieddate) VALUES ('alumni2', 'Alumni Page Block 2',
"<div class='hero-heading'><h1 style='color:#005440; text-align:center;'>What Have Alumni Been Up To?</h1></div><div class='card text-left green_back_gold_front mx-auto'><div class='card-body'><p style='font-size:22px' data-aos='fade-right' data-aos-duration='1000'>This section will be a few paragraphs long and have info regarding what the Alumni Association is and what Alumni in general have been doing. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco.</p><p style='font-size:22px' data-aos='fade-left' data-aos-duration='1000'>This section will be a few paragraphs long and have info regarding what the Alumni Association is and what Alumni in general have been doing. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco.</p></div></div><div class='space15'></div>",datetime('now'));

--join page content blocks
INSERT INTO cmspages (id, title, content, modifieddate) VALUES ('join_block1', 'Join Page - Block Why Us',
"<div class='col-lg-6'><div class='row g-3'><div class='col-6 text-end'><img class='img-fluid rounded w-75' data-aos='fade-down' data-aos-duration='1000' src='./static/img/p1.png' style='margin-top:0'></div><div class='col-6 text-start'><img class='img-fluid rounded w-100' data-aos='fade-left' data-aos-duration='1000' src='./static/img/p14.jpg'></div><div class='col-6 text-end'><img class='img-fluid rounded w-130' data-aos='fade-right' data-aos-duration='1000' src='./static/img/p16.jpg' style='margin-top:-60%'></div><div class='col-6 text-start'><img class='img-fluid rounded w-75' data-aos='fade-up' data-aos-duration='1000' src='./static/img/p17.jpg'></div></div></div><div class='col-lg-6'><div class='text-heading' data-aos='fade-down' data-aos-duration='1000'><h1>Why us?</h1></div><p style='font-size:22px' data-aos='fade-up' data-aos-duration='1000'>&#x2022; Sac State rowing lets you meet new individuals and make new friends. The friendships that you develop will stay with you throughout your life. The learnings that you gain through practice can be applied in various ways, such as in the classroom and in the real world. The community also extends beyond the country, state, and city limits.</p></div>",datetime('now'));
INSERT INTO cmspages (id, title, content, modifieddate) VALUES ('join_block2', 'Join Page - Second Block',
"<div class='col-lg-6'><p style='font-size:22px' data-aos='fade-right' data-aos-duration='1000'>&#x2022; You'll meet new people through the practice of rowing. The goal of the team is to build a close-knit environment where all members are dedicated to achieving success. We encourage a competitive environment and strive to improve the members' performance.</p><p style='font-size:22px' data-aos='fade-left' data-aos-duration='1000'>&#x2022; The goal of the program is to provide a challenging environment that pushes the members' physical and mental limits. Through the program, you'll have the opportunity to travel across the state and compete against other club teams across the country as well.</p></div><div class='col-md-6'><img class='img-fluid rounded w-100' data-aos='fade-down' data-aos-easing='ease-out-cubic' data-aos-duration='1000' src='./static/img/p15.png'></div>",datetime('now'));
INSERT INTO cmspages (id, title, content, modifieddate) VALUES ('join_block3', 'Join Page - Third Block',
"<div class='col-lg-6'><div class='text-heading'><h1 class='mb-4' data-aos='fade-right' data-aos-duration='1000'>Interested to Being a part of the Team?</h1></div><p style='text-align:center;font-size:22px' data-aos='zoom-in' data-aos-duration='1000'>All are welcome with<b>NO EXPERIENCE REQUIRED</b></p><div class='video-introduction-content-button'><a data-aos='fade-left' data-aos-duration='1000' href='https://docs.google.com/forms/d/e/1FAIpQLSfZgOi84FUsV-uXBSIsJuTX3pKZdlFydBgsojzrhYNo09q4ZA/formResponse'>Join us</a></div></div><div class='col-lg-6'><div class='row g-3'><div class='col-6 text-end'></div><div class='col-6 text-start'><img class='img-fluid rounded w-100' data-aos='zoom-in' data-aos-duration='1000' data-aos-delay='0' src='./static/img/p7.jpeg'></div><div class='col-6 text-end'><img class='img-fluid rounded w-100' data-aos='zoom-in' data-aos-duration='1000' data-aos-delay='200' src='./static/img/p8.jpeg' style='margin-top:-65%'></div><div class='col-6 text-start'><img class='img-fluid rounded w-75' data-aos='zoom-in' data-aos-duration='1000' data-aos-delay='400' src='./static/img/p6.jpeg'></div></div></div>",datetime('now'));
INSERT INTO cmspages (id, title, content, modifieddate) VALUES ('additional_info_donate', 'Additional Infomation Donation', 
"<div id='title-label4' class='name'>Additional Information</div><h2 class='extra-info' style='font-size:40px'>Additional<strong> Info</strong></h2><div class='name-phone'>Additional Information</div><div style='color:#000' style='font-weight:600' class='check'><h3><strong>Support the Sacramento State Rowing Club athletes in their journey to WIRAs.<br><em>The money will help fund activities such as:</strong><br>New Equipment, Team Gear, Scholarships, Team Travel,<br>Regatta Entry Fees, Coxswain Training.</div><h4 style='color:#005440'><br><strong>If you would like to donate via Check<br><em>Sac State Rowing Club<br>6000 J Street,<br>Sacramento, CA 95819</em></strong><div class='space80'></div></h4>",datetime('now'));
INSERT INTO cmspages (id, title, content, modifieddate) VALUES ('make_a_donation', 'Make A Donation', 
"<h2 class='text-uppercase mb-4' style='font-size:40px'>Make A<strong> Donation</strong></h2><p style='font-size:22px' class='mb-4'>You can help the Rowing Club by donating on our official donation page!<br>After clicking the link below,<strong>at Fund Designation: choose 'Rowing Club.'</strong></p>",datetime('now'));


-- Table for OTP log-in email storage
-- not currently implemented for use
-- change to rowingclub email once site is ready for release
CREATE TABLE IF NOT EXISTS loginEmail (
	emailHash VARCHAR(255) NOT NULL UNIQUE,
	otp VARCHAR(255) NOT NULL);


-- sql table for links (social media links)
CREATE TABLE IF NOT EXISTS links (
	id VARCHAR(255) NOT NULL UNIQUE,
	title VARCHAR(255) NOT NULL UNIQUE, 
	url VARCHAR(255) NOT NULL);

INSERT INTO links (id, title, url) VALUES ('joinusform', 'Join Us Form', 'https://docs.google.com/forms/d/e/1FAIpQLSfZgOi84FUsV-uXBSIsJuTX3pKZdlFydBgsojzrhYNo09q4ZA/viewform');
INSERT INTO links (id, title, url) VALUES ('instagram', 'Instagram', 'https://www.instagram.com/sacstaterowing/?utm_source=ig_embed&ig_rid=e3bcb0d8-a7ed-4db4-91de-788cbab2536c');
INSERT INTO links (id, title, url) VALUES ('flickr', 'Flickr', 'https://www.flickr.com/photos/199260406@N02/albums/72177720311662792');
INSERT INTO links (id, title, url) VALUES ('mailingform', 'Mailing List Form', 'https://forms.gle/4r7Mjue4fTxdWX716');
INSERT INTO links (id, title, url) VALUES ('donate', 'Donate','https://swarmfunding.csus.edu/project/36577/donate');
INSERT INTO links (id, title, url) VALUES ('donateaff', 'Donate to Affiliates','#');

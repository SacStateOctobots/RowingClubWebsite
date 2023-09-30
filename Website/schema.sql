-- a sample sql table
CREATE TABLE IF NOT EXISTS players (
	name VARCHAR(255) NOT NULL UNIQUE, 
	description VARCHAR(255) NOT NULL UNIQUE, 
	imgfilename VARCHAR(255) NOT NULL UNIQUE);
-- some sample inputs
INSERT INTO players (name, description, imgfilename) VALUES ('Player1', 'Hello, my name is Player1.','Cat1.jpg');
INSERT INTO players (name, description, imgfilename) VALUES ('Player2', 'Hello, my name is Player2.','Cat2.jpg');
INSERT INTO players (name, description, imgfilename) VALUES ('Player3', 'Hello, my name is Player3.','Cat3.jpg');
INSERT INTO players (name, description, imgfilename) VALUES ('Player4', 'Hello, my name is Player4.','Cat4.jpg');
INSERT INTO players (name, description, imgfilename) VALUES ('Player5', 'Hello, my name is Player5.','Cat5.jpg');

CREATE TABLE IF NOT EXISTS testimonials (
	name VARCHAR(255) NOT NULL UNIQUE, 
	testimonial VARCHAR(255) NOT NULL UNIQUE, 
	imgfilename VARCHAR(255) NOT NULL UNIQUE,
	job VARCHAR(255) NOT NULL UNIQUE);

INSERT INTO testimonials (name, testimonial, imgfilename,job) VALUES ('Spiderman', 'A testimonial from a
                            client who benefited from your product or service.
                            Testimonials can be a highly effective way of establishing
                            credibility and increasing your companys reputation.','https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Spider-Man.jpg/1200px-Spider-Man.jpg','superhero');

CREATE TABLE IF NOT EXISTS team_members (
    name VARCHAR(255) NOT NULL UNIQUE,
    team_member VARCHAR(255) NOT NULL,
    imgfilename VARCHAR(255) NOT NULL,
    role VARCHAR(255) NOT NULL
);

-- Insert team member data
INSERT INTO team_members (name, team_member, imgfilename, role) VALUES
	('Team Member 1', 'Hello, I am Team Member 1.', 'https://upload.wikimedia.org/wikipedia/commons/0/08/Astronotus_ocellatus.jpg', 'Role 1'),
	('Team Member 2', 'Hello, I am Team Member 2.', 'https://upload.wikimedia.org/wikipedia/commons/0/08/Astronotus_ocellatus.jpg', 'Role 2'),
    ('Team Member 3', 'Hello, I am Team Member 3.', 'https://upload.wikimedia.org/wikipedia/commons/0/08/Astronotus_ocellatus.jpg', 'Role 3'),
	('Team Member 4', 'Hello, I am Team Member 4.', 'https://upload.wikimedia.org/wikipedia/commons/0/08/Astronotus_ocellatus.jpg', 'Role 4'),
    ('Team Member 5', 'Hello, I am Team Member 5.', 'https://upload.wikimedia.org/wikipedia/commons/0/08/Astronotus_ocellatus.jpg', 'Role 5'),
    ('Team Member 6', 'Hello, I am Team Member 6.', 'https://upload.wikimedia.org/wikipedia/commons/0/08/Astronotus_ocellatus.jpg', 'Role 6'),
    ('Team Member 7', 'Hello, I am Team Member 7.', 'https://upload.wikimedia.org/wikipedia/commons/0/08/Astronotus_ocellatus.jpg', 'Role 7'),
    ('Team Member 8', 'Hello, I am Team Member 8.', 'https://upload.wikimedia.org/wikipedia/commons/0/08/Astronotus_ocellatus.jpg', 'Role 8'),
    ('Team Member 9', 'Hello, I am Team Member 9.', 'https://upload.wikimedia.org/wikipedia/commons/0/08/Astronotus_ocellatus.jpg', 'Role 9');

CREATE TABLE IF NOT EXISTS alumni (
	name VARCHAR(255) NOT NULL UNIQUE, 
	description VARCHAR(255) NOT NULL UNIQUE, 
	imgfilename VARCHAR(255) NOT NULL UNIQUE);	

INSERT INTO alumni (name, description, imgfilename) VALUES ('Alumni1', 'Hello, my name is Alumni1.','Cat1.jpg');
INSERT INTO alumni (name, description, imgfilename) VALUES ('Alumni2', 'Hello, my name is Alumni2.','Cat2.jpg');	

-- sql table for officers (about page)
CREATE TABLE IF NOT EXISTS officers (
	name VARCHAR(255) NOT NULL UNIQUE,
	desc VARCHAR(255) NOT NULL UNIQUE, 
	filename VARCHAR(255) NOT NULL);

INSERT INTO officers (name, desc, filename) VALUES 
('Officer1', 'This is test text for officer1.', 'https://upload.wikimedia.org/wikipedia/commons/7/7b/Quite_the_happy_dog.jpg'),
 ('Officer2', 'This is test text for officer2.', 'https://upload.wikimedia.org/wikipedia/commons/7/7b/Quite_the_happy_dog.jpg'),
 ('Officer3', 'This is test text for officer3.', 'https://upload.wikimedia.org/wikipedia/commons/7/7b/Quite_the_happy_dog.jpg'),
 ('Officer4', 'This is test text for officer4.', 'https://upload.wikimedia.org/wikipedia/commons/7/7b/Quite_the_happy_dog.jpg'),
 ('Officer5', 'This is test text for officer5.', 'https://upload.wikimedia.org/wikipedia/commons/7/7b/Quite_the_happy_dog.jpg'),
 ('Officer6', 'This is test text for officer6.', 'https://upload.wikimedia.org/wikipedia/commons/7/7b/Quite_the_happy_dog.jpg'),
 ('Officer7', 'This is test text for officer7.', 'https://upload.wikimedia.org/wikipedia/commons/7/7b/Quite_the_happy_dog.jpg'),
 ('Officer8', 'This is test text for officer8.', 'https://upload.wikimedia.org/wikipedia/commons/7/7b/Quite_the_happy_dog.jpg');

-- sql table for cmspages (about page)
CREATE TABLE IF NOT EXISTS cmspages (
	slug VARCHAR(255) NOT NULL UNIQUE,
	title VARCHAR(255) NOT NULL UNIQUE, 
	content TEXT NOT NULL,
	modifieddate VARCHAR(255));

INSERT INTO cmspages (slug, title, content, modifieddate) VALUES 
('aboutus', 'About Us', "<div class='col-lg-6'>
				<p style='font-size: 22px;' data-aos='fade-right' data-aos-duration='1000'> 
					&#x2022; Since 1984 the Sacramento State Men's Rowing team has competed
					against universities
					from all over the country. As part of the Western Intercollegiate Rowing Association, the
					team has won multiple conference championships in the Varsity 8. They also have had
					championship boats in several other events during the team’s history.
				</p>
				<p style='font-size: 22px;' data-aos='fade-left' data-aos-duration='1000'> &#x2022; The members of this
					team throughout history pride themselves on hard work, dedication, and commitment to
					a common goal. (Competition & Practice Schedules with be added soon) In 2021, the club
					transitioned to become the Rowing Club, now offering both men’s and women’s rowing.
				</p>
			</div>
			<div class='col-md-6' data-aos='fade-down' data-aos-duration='1000'>
				<img class='img-fluid rounded w-100' src='./static/img/p5.jpeg'>
			</div>",datetime('now'));
INSERT INTO cmspages (slug, title, content, modifieddate) VALUES ('social', 'Social Block',
"<div class='wrapper-social-icon'>
			<div class='button-social'>
				<div class='social-icon'>
					<em class='fab fa-facebook-f'>&nbsp;</em>
				</div>
				<a href='https://facebook.com'><span>Facebook</span></a>
			</div></a>
			<div class='button-social'>
				<div class='social-icon'>
					<em class='fab fa-instagram'>&nbsp;</em>
				</div>
				<a href='https://instagram.com'><span>Instagram</span></a>
			</div></a>
			<div class='button-social'>
				<div class='social-icon'>
					<em class='fab fa-youtube'>&nbsp;</em>
				</div>
				<a href='https://youtube.com'><span>YouTube</span></a>
			</div></a>
		</div>",datetime('now'));
INSERT INTO cmspages (slug, title, content, modifieddate) VALUES ('contact', 'Contact Information',
"<p style='color:black'>Have any questions?</p>
		<br>
		<p style='color:black;'>Email us at abcd@csus.com</p>",datetime('now'));
INSERT INTO cmspages (slug, title, content, modifieddate) VALUES ('contact_logo', 'Contact Logo',
"<div class='col-md-4' style='text-align: center;'>
                        <div class='contact-icon' data-aos='fade-down' data-aos-duration='1000'>
                            <div class='icon'>
                                <i class='fas fa-home'></i>
                            </div>
                            <h3>VISIT US</h3>
                            <p> We always welcome you at </p>
                            <h4>1901 Hazel Ave, <br> Gold River, CA 95670</h4>
                        </div>
                    </div>
                    <!--Phone Logo-->
                    <div class='col-md-4' style='text-align: center;'>
                        <div class='contact-icon' data-aos='fade-down' data-aos-duration='1000' data-aos-delay='300'>

                            <div class='icon'>
                                <i class='fas fa-phone'></i>
                            </div>
                            <h3>CALL US</h3>
                            <p> We are happy to hear from you </p>
                            <h4>+1 209 123 4567</h4>
                        </div>
                    </div>

                    <!--Email Logo-->
                    <div class='col-md-4' style='text-align: center;'>
                        <div class='contact-icon' data-aos='fade-down' data-aos-duration='1000' data-aos-delay='600'>
                            <div class='icon'> <i class='fas fa-envelope'></i>
                            </div>
                            <h3>Email US</h3>
                            <p> Even you can send us any messages</p>
                            <h4>rowing@abcd.csus.edu</h4>
                        </div>
                    </div>",datetime('now'));

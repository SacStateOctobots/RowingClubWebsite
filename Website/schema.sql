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

CREATE TABLE IF NOT EXISTS team_members (
    name VARCHAR(255) NOT NULL UNIQUE,
    description VARCHAR(255) NOT NULL,
    imgfilename VARCHAR(255) NOT NULL,
    role VARCHAR(255) NOT NULL);

-- Insert team member data
INSERT INTO team_members (name, description, imgfilename, role) VALUES
	('Team Member 1', 'Hello, I am Team Member 1.', 'Cat1.jpg', 'Role 1'),
	('Team Member 2', 'Hello, I am Team Member 2.', 'Cat2.jpg', 'Role 2'),
    ('Team Member 3', 'Hello, I am Team Member 3.', 'Cat3.jpg', 'Role 3'),
	('Team Member 4', 'Hello, I am Team Member 4.', 'Cat4.jpg', 'Role 4'),
    ('Team Member 5', 'Hello, I am Team Member 5.', 'Cat5.jpg', 'Role 5');

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
('Officer1', 'This is test text for officer1.', 'Cat1.jpg'),
 ('Officer2', 'This is test text for officer2.', 'Cat2.jpg'),
 ('Officer3', 'This is test text for officer3.', 'Cat3.jpg'),
 ('Officer4', 'This is test text for officer4.', 'Cat4.jpg'),
 ('Officer5', 'This is test text for officer5.', 'Cat5.jpg');

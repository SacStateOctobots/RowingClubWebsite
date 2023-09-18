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
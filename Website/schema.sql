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
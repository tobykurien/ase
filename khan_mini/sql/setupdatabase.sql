CREATE DATABASE if not exists ase;
CREATE USER 'ase'@'localhost' IDENTIFIED BY 'asep4s5';
GRANT ALL PRIVILEGES ON ase.* TO 'ase'@'localhost';
FLUSH PRIVILEGES;
USE ase;

drop table if exists admin;
create table admin (
 password varchar(255));

insert into admin values('54a2f7f92a5f975d8096af77a126edda7da60c5aa872ef1b871701ae');

drop table if exists assignment;
create table assignment (
 id INTEGER PRIMARY KEY AUTO_INCREMENT,
 title varchar(100),
 description varchar(255),
 state varchar(255),
 duration integer,
 startdatetime varchar(255)
);

drop table if exists essay;
create table essay(
 id INTEGER PRIMARY KEY AUTO_INCREMENT,
 assignment_id INTEGER REFERENCES assignment(id) ON DELETE CASCADE,
 student_name varchar(255),
 essay_text varchar(4096), 
 submitteddatetime varchar(255),
 score real,
 grade real);


drop table if exists comments; 
create table comments(
  id INTEGER PRIMARY KEY AUTO_INCREMENT, 
  essay_id INTEGER REFERENCES essay(id) ON DELETE CASCADE,
  comment_text varchar(4096),
  comment_type INTEGER, 
  submitteddatetime varchar(255),
  student_name varchar(255)
);
	

drop table if exists essay_eval;
create table essay_eval(
 id INTEGER PRIMARY KEY AUTO_INCREMENT,
 assignment_id INTEGER REFERENCES assignment(id) ON DELETE CASCADE,
 student_name varchar(255),
 essay1_id integer,
 essay2_id integer,
 essay3_id integer,
 score1 real,
 score2 real,
 score3 real 
);

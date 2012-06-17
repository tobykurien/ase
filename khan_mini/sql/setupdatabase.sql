PRAGMA foreign_keys = ON;

drop table if exists student;
create table student (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 student_name text);

drop table if exists quiz;
create table quiz (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 title text,
 description text,
 state text,
 date text
);

drop table if exists question;
create table question (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 quiz_id INTEGER REFERENCES quiz(id) ON DELETE CASCADE,
 questiontext text);


drop table if exists assignment;
create table assignment(
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 quiz_id INTEGER REFERENCES quiz(id) ON DELETE CASCADE,
 student_id INTEGER REFERENCES student(id) ON DELETE CASCADE,
 score real);

drop table if exists answer;
create table answer(
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 assignment_id INTEGER REFERENCES assignment(id) ON DELETE CASCADE,
 question_id INTEGER REFERENCES question(id) ON DELETE CASCADE,
 answer_text text);

drop table if exists eval;
create table eval(
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 quiz_id INTEGER REFERENCES quiz(id) ON DELETE CASCADE,
 question_id INTEGER REFERENCES question(id) ON DELETE CASCADE);

drop table if exists answerscore;
create table answerscore(
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 eval_id INTEGER REFERENCES eval(id) ON DELETE CASCADE, 
 answer_id INTEGER REFERENCES answer(id) ON DELETE CASCADE,
 student_id INTEGER REFERENCES student(id) ON DELETE CASCADE,
 score real);




#!/bin/sh
DIR=$(date +%Y%m%d)

mkdir $DIR
cd $DIR
echo Backing up www...
zip -r www.zip /var/www/moodle/* 2>/dev/null >/dev/null

echo Backing up database...
mysqldump -u moodleuser -phouse4hackp4s5 moodle > moodle.sql
zip mysql.zip  moodle.sql
rm moodle.sql

echo Backing up data...
zip -r moodledata.zip ~/moodle/moodledata/* 2>/dev/null >/dev/null

echo Done.


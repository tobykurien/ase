#!/bin/sh
HOME="/home/ubuntu/"
DIR=$HOME"moodle/backups/$(date +%a)"
echo $DIR

mkdir $DIR
cd $DIR
#echo Backing up www...
#zip -r www.zip /var/www/moodle/* 2>/dev/null >/dev/null

echo Backing up database...
mysqldump -u moodleuser -pmoodlepass moodle > moodle.sql
zip mysql.zip  moodle.sql
rm moodle.sql

echo Backing up data...
zip -r moodledata.zip ~/moodle/moodledata/* 2>/dev/null >/dev/null

echo Uploading backups...
rsync -ar $DIR ubuntu@cloud.house4hack.co.za:~/moodle/ase_backups

echo Done.


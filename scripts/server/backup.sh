#!/bin/sh
HOME="/home/ubuntu/moodle/backups"
DIR=$HOME"/$(date +%a)"
echo $DIR

mkdir $DIR
cd $DIR
#echo Backing up www...
#zip -r www.zip /var/www/moodle/* 2>/dev/null >/dev/null

echo Backing up moodle database...
mysqldump -u moodleuser -pmoodlepass moodle > moodle.sql
zip mysql.zip  moodle.sql
rm moodle.sql

echo Backing up peer marker database...
mysqldump -u ase -pasep4s5 ase > ase.sql
zip ase.zip  ase.sql
rm ase.sql

#echo Backing up khan academy database...
#cp /home/ubuntu/khan_academy/code/datastore /home/ubuntu/khan_academy/code/datastore.backup
#zip ka_datastore.zip /home/ubuntu/khan_academy/code/datastore.backup

#echo Backing up data...
#zip -r moodledata.zip /home/ubuntu/moodle/moodledata/* >/dev/null

echo Uploading backups...
rsync -ar --progress $HOME ubuntu@cloud.house4hack.co.za:~/moodle/ase_backups

echo Done.


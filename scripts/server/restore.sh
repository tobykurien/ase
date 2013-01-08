#!/bin/sh
rm -rf tmp
mkdir tmp

sudo mv moodledata tmp
unzip moodledata.zip
mv home/ubuntu/moodle/moodledata ./
rm -rf home
sudo chmod www-data:www-data moodledata

cd tmp
unzip ../mysql.zip
msql -u moodleuser -pmoodlepass moodle < mysql.sql

cd ..


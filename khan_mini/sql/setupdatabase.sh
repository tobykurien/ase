#mkdir ../db
#--rm ../db/englishessay.db
#sqlite3 ../db/englishessay.db < setupdatabase.sql   
#sqlite3 ../db/englishessay.db < loadsampledata.sql   
echo "Creating the database on mysql using root - enter the password for the root user on mysql"
mysql -u root -p < setupdatabase.sql   
echo "Populating with test data - enter the password for the 'ase' user - should be asep4s5"
mysql -u ase -p ase < loadsampledata.sql   

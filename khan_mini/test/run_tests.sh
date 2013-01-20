#!/bin/sh
echo "Resetting database, enter password for ase user on database (WARNING: database will be wiped!)"
#while [ 1 ]
#do
mysql -u ase -p < ../sql/setupdatabase.sql   
python peer_marker1.py
#done


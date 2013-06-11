#!/bin/sh
echo Resetting Khan Academy...
cd /home/ubuntu/khan_academy
killall python
sleep 10s
rm code/datastore.broken
mv code/datastore code/datastore.broken
cp code/datastore.original code/datastore
echo Done. Restarting Khan Academy...
./run



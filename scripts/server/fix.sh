#!/bin/sh
cd khan_academy/code
sudo killall -9 python
rm datastore
cp datastore.original datastore
cd ..
./run


#!/bin/sh
sudo ifconfig eth0 192.168.0.32 up

cd /home/ubuntu/ase/khan_mini
nohup python index.py &

cd /home/ubuntu/khan_academy
nohup ./run &

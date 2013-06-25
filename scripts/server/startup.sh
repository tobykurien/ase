#!/bin/sh
ifconfig eth0 192.168.1.2 up
route add default gw 192.168.1.1
echo "domain africanschoolforexcellence.org" > /etc/resolv.conf
echo "search africanschoolforexcellence.org" >> /etc/resolv.conf
echo "nameserver 192.168.1.1" >> /etc/resolv.conf
echo "nameserver 8.8.8.8" >> /etc/resolv.conf

cd /home/ubuntu/ase/khan_mini
nohup ./run &

cd /home/ubuntu/khan_academy
./run &

/home/ubuntu/house4hack_tunnel.sh &


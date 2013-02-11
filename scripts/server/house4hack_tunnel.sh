#!/bin/sh
autossh -M 2210 -N -f -R 2211:localhost:22 -R 2212:localhost:80 -R 2213:localhost:8080 -R 2214:localhost:8081 cloud.house4hack.co.za


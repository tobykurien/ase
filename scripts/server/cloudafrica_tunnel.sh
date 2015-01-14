#!/bin/sh
autossh -M 0 -N -f -R 2211:localhost:22 -R 2212:localhost:80  ase@cloud.tobykurien.com -p 2222

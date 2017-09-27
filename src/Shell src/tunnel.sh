#!/bin/sh

autossh -N -o 'PubkeyAuthentication=yes' -o 'PasswordAuthentication=no' -i /home/pi/.ssh/nopwd -R 3329:localhost:22 bao2@gwip.cooper.edu -p 8199 &

#!/bin/bash

sudo airmon-ng start wlan1

#sudo timeout 30 airodump-ng mon0 -w mydump --update 30 -o csv
{ sudo airodump-ng wlan1  -w mydump --update 180 -o csv; } &

# 20 per hour, 960 for 48 hours or 2 days
for (( i=0; i<960; i++ ))
do
	sudo tshark -a duration:30 -S -l -i mon0 -Y 'wlan.fc.type_subtype eq 4' -T fields -e frame.time -e wlan.sa_resolved -e wlan_mgt.ssid >> probe.csv
	sleep 180

done

sudo airmon-ng stop mon0
sudo airmon-ng stop wlan1
sudo killall airodump-ng 

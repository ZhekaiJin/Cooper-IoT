#!/bin/bash

for (( i=0; i<10; i++ ))
do
	sudo tshark -a duration:30 -S -l -i mon0 -Y 'wlan.fc.type_subtype eq 4' -T fields -e frame.time -e wlan.sa_resolved -e wlan_mgt.ssid >> probe.csv
	sleep 180
done

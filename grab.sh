#! /bin/bash

#cd ../rawdata

# vehicle IP address
#V_IP_File='../vip/ip.txt'

V_IP_File='../ip.txt'

while read -r line
do
    vehicle_IP="$line"
    wget -r -nd "http://$vehicle_IP:9000"
    if [ -e 'index.html' ]
    then
      rm index.html
    fi
done < "$V_IP_File"

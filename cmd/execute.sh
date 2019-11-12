#!/bin/bash

IP_File='host'
vehicle_IP=()
i=0

while read -r line
do
  vehicle_IP[$i]="$line"
  let "i++"
done < "$IP_File"

for ip in "${vehicle_IP[@]}"
do
#  sshpass -f paswd scp -r broadcast/ $ip:~/Desktop/
#  sshpass -f paswd scp -r subscribe/ $ip:~/Desktop/
#  sshpass -f paswd scp -r desired_images/ $ip:~/Desktop/
#  sshpass -f paswd scp -r output/ $ip:~/Desktop/
#  sshpass -f paswd scp auto_test.sh $ip:~/Desktop/
#  sshpass -f paswd scp n2otest.sh $ip:~/Desktop/
#  sshpass -f paswd scp grab.sh $ip:~/Desktop/
#  sshpass -f paswd scp wget_test.sh $ip:~/Desktop/
  sshpass -f paswd scp read_time.py $ip:~/Desktop/
done

#!/bin/bash

i=1
NUMBER_of_TEST=3

while [ $i -lt $NUMBER_of_TEST ]
do
  logfile="log$i"

  sshpass -f paswd parallel-ssh -h pssh-hosts -o log/$logfile -A -I < pssh-commands

  let "i++"
  read -p "enter to continue..."
done

echo "test ended"

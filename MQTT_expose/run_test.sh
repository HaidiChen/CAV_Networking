#!/bin/bash

i=1
NUMBER_of_TEST=1

while [ $i -le $NUMBER_of_TEST ]
do
  logfile="log$i"

  sshpass -f paswd parallel-ssh -h pssh-hosts -o log/$logfile -A -I < pssh-commands -t 10000

  echo "Test: $i finished"
  let "i++"
done 

echo 'test ended'

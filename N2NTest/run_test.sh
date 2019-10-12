#!/bin/bash

i=1

while [ $i -lt 5 ]
do
  logfile="log$i"

  sshpass -f paswd parallel-ssh -h pssh-hosts -o log/$logfile -P -A -I < pssh-commands

  let "i++"
done

#! /bin/bash

if [ -e 'broadcast_time.txt' ]
then
  rm broadcast_time.txt
fi

touch broadcast_time.txt

cd broadcast/

(time python3 main.py) &> ../broadcast_time.txt

cd ..

python3 read_time.py


if [ -e 'n2otest.sh' ]
then
  bash n2otest.sh
fi

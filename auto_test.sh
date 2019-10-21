#! /bin/bash

cd broadcast/
python3 main.py

sleep 20

cd ~/Desktop/

if [ -e 'n2otest.sh' ]
then
  bash n2otest.sh
fi

#!/bin/bash

rm output/*
if [ -e 'broadcast_time.txt' ]
then
  rm broadcast_time.txt
fi

touch broadcast_time.txt

cd output/
mv ../grab.sh .

(time bash grab.sh) &> ../broadcast_time.txt

mv grab.sh ../
cd ..

python3 read_time.py 

tree output/ | tail -1

python3 compare.py -i desired_images/ -ii output/

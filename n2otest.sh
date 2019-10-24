#!/bin/bash

#while [ 1 ]
#do
#  	read -p "enter to continue..." 

	tree output/ | tail -1

  	python3 compare.py -i desired_images/ -ii output/

	rm output/*
#done

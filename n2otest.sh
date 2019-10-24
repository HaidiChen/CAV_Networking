#!/bin/bash

tree output/ | tail -1

python3 compare.py -i desired_images/ -ii output/

rm output/*

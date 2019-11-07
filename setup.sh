#! /bin/bash

sudo apt update
sudo apt -y upgrade

sudo apt install python3
sudo apt install python3-pip
pip3 install -r requirements.txt

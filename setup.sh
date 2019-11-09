#! /bin/bash

sudo apt update
sudo apt -y upgrade

sudo apt install -y python3
sudo apt install -y python3-pip
pip3 install -r requirements.txt

sudo apt install -y tree

#! /bin/bash

# check if broker IP file exists
if [ ! -e 'bip/ip.txt' ]
then
	echo 'bip/ip.txt missing'
	exit 1
fi

# delete all stopped containers
docker rm $(docker ps -a -q)

# create directories
if [ -d "shared_folder" ]
then
	rm -rf shared_folder
fi

if [ -d "feedback" ]
then
	rm -rf feedback
fi
mkdir shared_folder
mkdir feedback

# run docker containers
cd shared_folder
#docker run -v `pwd`:/mydata -p 9000:9000 -p 3000:3000 -d thatape/ecf_vehicle:expose /mydata 
docker run -v `pwd`:/mydata -p 9000:9000 -p 3000:3000 -d st571332/ecf_vehicle:expose /mydata 

cd ../bip
brokerip_path=`pwd`

#cd ../feedback
#docker run --network host -v `pwd`:/output -v $brokerip_path:/bip -d thatape/ecf_vehicle:feedback
#docker run --network host -v `pwd`:/output -v $brokerip_path:/bip -d st571332/ecf_vehicle:feedback

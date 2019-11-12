### install the docker on Linux ###

# update the packages
sudo apt-get update

# install the prerequisite packages
sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common

# add the GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"

sudo apt-get update

apt-cache policy docker-ce

sudo apt-get install -y docker-ce

# add user to the docker group
sudo usermod -aG docker ${USER}

#sudo systemctl status docker

#su - ${USER}

# confirm the user is in the group
#id -nG

### test docker installation ###
docker run hello-world




#!/bin/bash
#elaborado por sinfallas
if [ $USER != root ]; then
echo "Error: debes ser root"
exit 1
fi
echo "deb http://liquorix.net/debian sid main" >> /etc/apt/sources.list
add-apt-repository -y ppa:ubuntu-toolchain-r/test
apt update
apt -y install liquorix-keyrings gcc-4.7
apt update
apt -y install linux-image-liquorix-amd64 linux-headers-liquorix-amd64
clear
echo Finalizado se recomienda reiniciar.
exit 0
#!/bin/bash
apt update
apt -y --force-yes dist-upgrade
apt-get clean
apt-get autoremove
rm -rf /tmp/*
rm -rf /var/tmp/*
echo -e "\e[00;1;92mFinished...\e[00m"
exit 0

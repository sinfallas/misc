#!/bin/bash
apt update
apt -y --force-yes dist-upgrade
apt-get clean
apt -y autoremove
rm -rf /tmp/*
rm -rf /var/tmp/*
exit 0

#!/bin/bash
apt update
apt -y --force-yes dist-upgrade
apt-get clean
apt -y autoremove
exit 0

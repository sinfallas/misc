#!/bin/bash
#elaborado por sinfallas
if [[ $USER != root ]]; then
echo -e "\e[00;31mERROR: DEBES SER ROOT\e[00m"
exit 1
fi
service squid3 stop
rm -rfv /var/spool/squid3/*
squid3 -z
service squid3 restart
echo "finalizado"
exit 0

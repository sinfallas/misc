#!/bin/bash
#elaborado por sinfallas
if [[ $USER != root ]]; then
echo -e "\e[00;31mERROR: DEBES SER ROOT\e[00m"
exit 1
fi
page_size=$(getconf PAGE_SIZE)
phys_pages=$(getconf _PHYS_PAGES)
shmall=`expr $phys_pages / 2`
shmmax=`expr $shmall \* $page_size`
echo kernel.shmmax = $shmmax >> /etc/sysctl.conf
echo kernel.shmall = $shmall >> /etc/sysctl.conf
echo kernel.shmmax = $shmmax
echo kernel.shmall = $shmall
exit 0

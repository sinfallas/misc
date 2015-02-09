#!/bin/bash
modprobe zram
echo $((100*1024*1024)) > /sys/block/zram0/disksize
mkswap /dev/zram0
swapon /dev/zram0
exit 0

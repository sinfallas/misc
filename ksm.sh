#!/bin/sh -e
echo "1" > /sys/kernel/mm/ksm/run
echo "20000" > /sys/kernel/mm/ksm/pages_to_scan
echo "200" > /sys/kernel/mm/ksm/sleep_millisecs
exit 0

#!/bin/bash
# Made by Sinfallas <sinfallas@yahoo.com>
# Licence: GPL-2
#bloquea un proceso para que no se ejecute simultaneamente
randa=$(($RANDOM%3+1))
pid_run=$(ps -eo pid,comm | grep $0 | egrep -o '[0-9]+' )
if [[ "${pid_run:-NO_VALUE}" != "NO_VALUE" ]] ; then 
   echo "$0 $@" | ahora + $randa minutos
   exit
fi
exit 0

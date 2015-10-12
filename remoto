#!/bin/bash
# Made by Sinfallas <sinfallas@yahoo.com>
# Licence: GPL-2
HOST="aqui_pon_la_maquina_remota"
USER="aqui_pon_el_usuario_remoto"
PASS="aqui_pon_el_password_remoto"
CMD=$@
VAR=$(expect -c "
spawn ssh -o StrictHostKeyChecking=no $USER@$HOST $CMD
match_max 100000
expect \"*?assword:*\"
send -- \"$PASS\r\"
send -- \"\r\"
expect eof
")
echo "==============="
echo "$VAR"
exit 0

#!/bin/sh
printf "Content-Type: text/plain\r\n\r\n"
decode=`sh decode.sh ${QUERY_STRING}`
ls -A -p ../${decode}

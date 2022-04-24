#!/bin/bash
# USAGE: script_bash.sh [source.dat] [newfile.dat]

if test -f $2; then
rm $2
fi

echo "Time Port" >> $2

cat $1 | tr -s ' ' | cut -d ' ' -f 3,10 | tail -n +2 >>  $2
#!/bin/bash

if test -f "temp_result_ping.txt"; then
    rm "temp_result_ping.txt"   
fi

echo "Size RttMin RttAvg RttMax" >> temp_result_ping.txt

#Per il Dongle Ethernet e' stato utilizzata un'altra sequenza

sequ="$(seq 0 1 15) $(seq 16 100 1450) $(seq 1460 1 1520) $(seq 1600 100 16000)"

for i in $sequ; do
    tmp=$(ping -c 10 -s $i -i 0.2 172.16.1.2 | grep "rtt" | cut -d ' ' -f 4 | cut -d '/' -f 1,2,3 --output-delimiter ' ')
    echo $i $tmp >> temp_result_ping.txt
done

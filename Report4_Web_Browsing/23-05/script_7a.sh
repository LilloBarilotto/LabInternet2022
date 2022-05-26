#!/bin/bash

numberTotalTransactionHTTP=$(grep httpVersion har.js | wc | tr -s ' ' |cut -d ' ' -f 2)
request=$(grep request har.js | wc | tr -s ' ' | cut -d ' ' -f 2)
response=$(grep response har.js | wc | tr -s ' ' |cut -d ' ' -f 2)

echo "7.a" 
echo "#TransactionHTTP = " $numberTotalTransactionHTTP
echo "#request = " $request
echo "#response = " $response

# tmp= $(grep mimeType har.js | sort | tr -s ' ' | cut -d ' ' -f 3 | tr -d '"'| tr -d ',')
# for (i in $( $tmp) ) do
   # grep -c $i 
# done,   alllora poi lo riscrivi come ti piace a te senza leggere piu volte il file ciao

uniq_res=$(grep '"mimeType":' har.js | sort | tr -s ' ' | cut -d ' ' -f 3 | tr -d '"'| tr -d ',' | uniq -c)

echo ""
echo "7.b"
echo "Type of mimeType"
echo $uniq_res

echo "" 
serverIP=$(grep serverIPAddress har.js | sort | uniq | wc | tr -s ' ' |cut -d ' ' -f 2)
echo "7.c #serverIPAddress =" $serverIP


bodySize=$(grep "bodySize" har.js | tr -s ' ' | cut -d ' ' -f 3 | tr -d ',')
totalSize=0

for i in $bodySize; do
    if [ "$i" != "-1" ]; then
        let totalSize+=$i
    fi
done

echo ""
echo "7.d TotalSize = " $totalSize
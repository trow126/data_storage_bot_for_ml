#!/bin/sh

cd `dirname $0`

for exchange in bybit binance coinbasepro ftx
do
    PROCESS_NAME="python3 main.py $exchange"

    count=`pgrep -f "${PROCESS_NAME}" | wc -l`
    if [ $count = 0 ]; then
        DATE=`date '+%Y-%m-%d %H:%M:%S'`
        $PROCESS_NAME &
        echo "$DATE '${PROCESS_NAME}' is start" >> check_process_log.log
    fi
done

exit
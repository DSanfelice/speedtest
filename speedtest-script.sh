#!/bin/bash

while true
do
    date +"%H%M" >> speedtest_time.txt
    speedtest >> speedtest.txt
    echo " "
    echo " "
    sleep 60
done
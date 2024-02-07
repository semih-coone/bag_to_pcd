#!/bin/bash

roscore &

sleep 5

python3 /convert_pcd.py

kill $(jobs -p)
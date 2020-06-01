#!/bin/bash

mkdir /flag
cd /flag
echo "$SSRF_FLAG" > flag.txt
python -m http.server 80 &

/usr/sbin/xinetd -dontfork

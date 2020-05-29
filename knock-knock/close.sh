#!/bin/bash
sed -i /etc/xinetd.d/flag -e "s/ $1//"
kill -s 1 `pidof xinetd`

#!/bin/bash
sed -i /etc/xinetd.d/flag -e "s/\(only_from.*\)/\1 $1/"
kill -s 1 `pidof xinetd`

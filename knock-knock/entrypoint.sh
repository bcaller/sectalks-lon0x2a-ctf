#!/bin/bash
set -x

/usr/sbin/xinetd -dontfork &
knockd --debug

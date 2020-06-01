#!/bin/bash
set -eu
ZWNJ_FLAG=${ZWNJ_FLAG:-flag\{b4n4n4_br34d\}}
ENCODED_A=$(./encodeflag.py "/SECURE/ANTI-WHISTLEBLOWER/${ZWNJ_FLAG:0:7}")
ENCODED_B=$(./encodeflag.py "${ZWNJ_FLAG:7}/UNAUTHORISED/BLOWING/OF/WHISTLE/")
OTHER=$(./encodeflag.py "/RETRIEVED/2020-05-28/")
sed -e "s/\*/$ENCODED_A/" -e "s/\*/$ENCODED_B/" -e "s/@/$OTHER/" template.txt | tee challenge.txt

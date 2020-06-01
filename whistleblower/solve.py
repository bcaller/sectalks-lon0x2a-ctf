#!/usr/bin/env python3
import sys

input = sys.stdin.read()
output = []

i = 0
while i < len(input):
    c = input[i]
    if c in ['\U0000200C', '\U0000200D']:
        bits = input[i:i + 8].replace('\U0000200C', '0').replace('\U0000200D', '1')
        output.append(chr(int(bits, 2)))
        i += 7
    i += 1

print("".join(output))

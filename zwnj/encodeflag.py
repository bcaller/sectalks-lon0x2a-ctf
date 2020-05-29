#!/usr/bin/env python3
import sys
flag = sys.argv[1]
print("".join("{:08b}".format(x) for x in flag.encode()).replace("0", "\U0000200C").replace("1", "\U0000200D"))

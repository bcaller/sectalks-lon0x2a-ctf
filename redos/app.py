#!/usr/local/bin/python -u

import os
import re
import sys


REGEXES = [
    r"""^
    (\d\d?)            # day
       (?:\s+|[-\/])
    (\w+)              # month
        (?:\s+|[-\/])
    (\d+)              # year
    (?:
          (?:\s+|:)    # separator before clock
       (\d\d?):(\d\d)  # hour:min
       (?::(\d\d))?    # optional seconds
    )?                 # optional clock
       \s*
    ([-+]?\d{2,4}|(?![APap][Mm]\b)[A-Za-z]+)? # timezone
       \s*
    (?:\(\w+\))?       # ASCII representation of timezone in parens.
       \s*$""",
]


if __name__ == '__main__':
    r = REGEXES[int(sys.argv[1])]
    REGEX = re.compile(r, re.X if '\n' in r else 0)
    if len(sys.argv) != 3:
        print(REGEX.pattern)
    else:
        attempt = os.environ["ATTEMPT"]
        print(">>>", attempt)
        if re.search(REGEX, attempt):
            print('Regex satisfied :)')
            print("You might expire then, but you aren't getting a flag.")
        else:
            print('Regex unsatisfied :(')

#!/usr/bin/env python
import string
import socket
import urllib.request
from time import sleep
from urllib.parse import urlparse

print("Enter URL to GET")
urlstr = input()
parsed = urlparse(urlstr)
assert parsed.scheme in ['http', 'https'], "Scheme not http(s)"
assert '.' in parsed.netloc, "Hostname does not contain a dot"
hexdot = string.hexdigits + '.'
assert any(c not in hexdot for c in parsed.netloc), "Hostname only contains hexademical characters and dots"
resolved = socket.gethostbyname(parsed.netloc)
assert resolved != "127.0.0.1", "Cannot resolve to localhost"
print("Getting from ", resolved)
for i in range(3):
    print(3 - i, flush=True)
    sleep(1)
with urllib.request.urlopen(urlstr) as f:
    print(f.info())
    print(f.read(321))

import base64
import random
import sys

super_secure_xor_key = bytearray(random.getrandbits(8) for _ in range(60))
print(super_secure_xor_key)


def xor(plain, key=super_secure_xor_key):
    return bytes(s ^ k for s, k in zip(plain, super_secure_xor_key))

def encode(plain, key=super_secure_xor_key):
    return base64.b64encode(base64.b64encode(xor(plain)))

# cat tokens.clear | python3 encode.py | tee tokens.xored
for line in sys.stdin.readlines():
    print(encode(line.encode()).decode())

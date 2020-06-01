import sys

input = sys.stdin.buffer
while True:
    try:
        a, b = input.read(2)
        sys.stdout.buffer.write(bytes((b,a)))
    except ValueError:
        break

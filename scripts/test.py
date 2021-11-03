from binascii import unhexlify
from sys import argv
with open('./produce.py') as m:
    file = bytes(m.read().encode()).hex()
    # exec(compile(unhexlify(file).decode(), '', 'exec'))
    print(file)
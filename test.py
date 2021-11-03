from ecdsa import SigningKey, VerifyingKey
from binascii import unhexlify
from jsonpickle import decode
from pickle import dumps
with open('./blocks/block_1/jsoschon.json') as jsoschon:
    data = decode(jsoschon.read()).hashSign
    vk = VerifyingKey.from_string(unhexlify('906ace857b46875ca180feb3c53b38a35e7f06cd8af2f19df9ebe18daf6d7cdd70404c7ca364b9796cc80601b26a8d1e'))
    print(vk.verify(unhexlify('f5b4a53b1c4c0d2b42353f8c27f8e70d27154f0a7b339fe0a4c36c3d003c09af329daa055b038d9072ab4b2d574cc6cc'), dumps(data)))

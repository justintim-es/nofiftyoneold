from ecdsa import SigningKey
from binascii import hexlify, unhexlify

from ecdsa.keys import VerifyingKey
from block import Block, GenesisProduce
from jsonpickle import encode, decode 
from pickle import dumps
from hashlib import sha512
from blockchain import Blockchain                                
# from bloc import Blockchain
sk = SigningKey.generate()
# print(hexlify(sk.to_string()).decode())
# print(sk.to_string().hex())
# sk2 = SigningKey.from_string(unhexlify(sk.to_string().hex()))
# print(sk2.to_string().hex())
# print(sk2.get_verifying_key().to_string().hex())
# signature = sk2.sign(b'h')
# signature_hex = hexlify(signature).decode()
# vk = VerifyingKey.from_string(unhexlify(sk2.get_verifying_key().to_string().hex()))
# vk: VerifyingKey = sk2.get_verifying_key()
# print(vk.verify(unhexlify(signature_hex), b'h'))
# sk1 = SigningKey.from_string(sk.to_string())
blockchain = Blockchain('blocks', sk.get_verifying_key().to_string().hex())
print(encode(blockchain.blocks[0]))
print(sk.get_verifying_key().to_string().hex())
# print(encode(blockchain.blocks[0]))
# block = GenesisProduce('blocks', sk.get_verifying_key().to_string().hex())
# print(block.gladiators[0].outputs[0].heschex)
# print(block.new_hash)
# print(block.nonce)
# print(sha512(dumps(block)).hexdigest())
# for i in range(10):
#     print(i)    
# with open('./blocks/block_0/jsoschon.json') as jsoschon:
#     block = decode(jsoschon.read())
#     print(block.new_hash)
#     print(sha512(dumps(block)).hexdigest())
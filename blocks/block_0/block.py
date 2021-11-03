from hashlib import sha256, sha512
from pickle import dumps as pdumps
from jsonpickle import decode, encode
from secrets import token_hex
from ecdsa import SigningKey, VerifyingKey
from os import mkdir, path, walk
from json import dumps as jdumps
from binascii import hexlify, unhexlify
from enum import Enum
from threading import Thread
from utils import get_spendable_outputs, get_last_total_difficulty
# een account moet tokens kosten omdat anders iedereen altijd zn geld verplaatst naar de nieuwste gladiator
# hij moet even duur zijn als de output van een gladiator met het hoogste saldo van alle public keys
# niet van alle public keys maar gewoon van de rijkste free/reproduce money account
class TransactionInput:
    def __init__(self, transaction_id, output_index, signature):
        self.transaction_id = transaction_id
        self.output_index = output_index
        self.signature = signature
class GladiatorTransactionInput(TransactionInput):
    def __init__(self, transaction_id, output_index, signature, gladiator_id):
        super().__init__(transaction_id, output_index, signature)
        self.gladiator_id = gladiator_id

# class TransactionOutput:
#     def __init__


class GladiatorOutput:
    def __init__(self, heschex, public_keys):
        self.heschex = heschex
        self.public_keys = public_keys

# kan echt zo zijn want het block contained the gladiator its hexadecimal signature_of_block
#you can verify the amount of outputs being created
# each node needs to have a set amount of peers
# its save because first of all why wouldn't you use all mining power on your own gladiator to make him stronger
# second of all if more computers put mining power on that gladiator the the more computers have a valid block
# so they all have to give a random value and something needs to keep track of all the random numbers
# we need the public_key_count to verify the blocks amount of created tx inputs and outputs
# so each transaction needs its own id
class GladiatorInput:
    def __init__(self, gladiator_id_cracked, output_index_cracked, signature_of_block_signs_output, signature_of_block):
        self.gladiator_id_cracked = gladiator_id_cracked
        self.output_index_cracked = output_index_cracked 
        self.public_key_count_cracked, self.public_key_count_cracker = self.get_public_key_count()
        self.signature_of_block_signs_output = signature_of_block_signs_output 
        sk = SigningKey.generate()
        vk = sk.get_verifying_key()
        
        self.private_key = sk.to_string().hex()
        self.public_key = sk.get_verifying_key().to_string().hex()
    def get_public_key_count(self, dir, gladiator_id_cracked, gladiator_id_cracker):
        _, _, files = walk(next('./' + dir))
        public_key_count_cracked = 0
        public_key_count_cracker = 0
        for i in range(len(files)):
            with open('./' + dir + '/block_' + str(i) + '/jsoschon.json') as jsoschon:
                block = encode(jsoschon.read()) 
                
                for gladiator in block.gladiators:
                    if gladiator.id == gladiator_id_cracked:
                        for public_key in gladiator.outputs[0].public_keys:
                            public_key_count_cracked += 1
                
        return public_key_count_cracked, public_key_count_cracker
                

class Gladiator:
    def __init__(self, outputs, inputs):
        self.outputs = outputs
        self.inputs = inputs
        self.id = sha512(pdumps(self)).hexdigest()
class Script(Enum):
    JSON = 1
    PRODUCE = 2
    STAB = 3
    REPRODUCE = 4 
class HashSign:
    def __init__(self, script, block_number=0, difficulty=0, total_difficulty=0, prev_hash=''):
        self.script: Script = script
        self.prev_hash = prev_hash
        self.block_number = block_number
        self.difficulty = difficulty
        self.total_difficulty = total_difficulty+difficulty
        sk = SigningKey.generate()
        self.private_key = sk.to_string().hex()
        self.public_key = sk.get_verifying_key().to_string().hex()
        self.nonce = -1
    def add_signature(self, private_key):
        sk = SigningKey.from_string(unhexlify(private_key))
        return hexlify(sk.sign(pdumps(self))).decode()
    def add_gladiators(self, gladiators):
        self.gladiators = gladiators

class Block:
    # genesis
    # free reproduce transaction parameter
    def __init__(self, dir, script, block_number=0, difficulty=0, prev_hash=''):
        self.hashSign = HashSign(script, block_number, difficulty, get_last_total_difficulty(dir), prev_hash) 
        self.create_dir(dir)
        self.save_json_ipc(dir)
        self.save_produce_ipc(dir)
        self.create_package(dir)
        

    def get_gladiator_hex(self):
        if self.hashSign.difficulty > 0:
            start = self.hashSign.prev_hash[:self.hashSign.difficulty]
            print(start)
            start = str(start) + token_hex(1)[:1]
            print('wentintonew', start)
            return start
        else:
            print('wenintobla')
            return token_hex(1)[:1]
    def create_dir(self, dir):
        if not path.exists('./' + dir + '/block_' + str(self.hashSign.block_number)):
            if not path.exists('./' + dir):
                mkdir(dir)
            mkdir(dir + '/block_' + str(self.hashSign.block_number))
    def create_package(self, dir):
        with open('./' + dir + '/block_' + str(self.hashSign.block_number) + '/package.json', 'w') as package:
            package.write(jdumps({
                "scripts": {
                    "json": "python -c \"from binascii import unhexlify; exec(compile(unhexlify(open('./jsoschon.txt').read()).decode(), '', 'exec'))\"",
                    "produce": "python -c \"from binascii import unhexlify; exec(compile(unhexlify(open('./produce.txt').read()).decode(), '', 'exec'))\" --public_key",
                    "stab": "",
                    "reproduce": "",
                }
            }))
    def save_json_ipc(self, dir):
        with open('./' + dir + '/block_' + str(self.hashSign.block_number) + '/jsoschon.txt', 'w') as jsoschon:
            jsoschon.write('0a77697468206f70656e28272e2f6a736f7363686f6e2e6a736f6e2729206173206a736f7363686f6e3a0a202020207072696e74286a736f7363686f6e2e72656164282929202020200a202020')
    def save_produce_ipc(self, dir):
        with open('./' + dir + '/block_' + str(self.hashSign.block_number) + '/produce.txt', 'w') as produce:
            produce.write('66726f6d20626c6f636b20696d706f72742047656e6573697350726f647563650a66726f6d206f7320696d706f72742077616c6b0a66726f6d20617267706172736520696d706f727420417267756d656e745061727365720a66726f6d206a736f6e7069636b6c6520696d706f727420656e636f64652c206465636f64650a6172675f706172736572203d20417267756d656e7450617273657228290a6172675f7061727365722e6164645f617267756d656e7428272d2d7075626c69635f6b6579272c2072657175697265643d54727565290a6173636861726773203d206172675f7061727365722e70617273655f6172677328290a5f2c20646972732c205f203d206e6578742877616c6b28272e2e2f2729290a77697468206f70656e28272e2e2f626c6f636b5f27202b20737472286c656e2864697273292d3129202b20272f6a736f7363686f6e2e6a736f6e2729206173206a736f7363686f6e3a0a20202020707265765f626c6f636b203d206465636f6465286a736f7363686f6e2e726561642829290a20202020626c6f636b203d2047656e6573697350726f6475636528272e2e2f272c2061736368617267732e7075626c69635f6b65792c206c656e2864697273292c20707265765f626c6f636b2e6e65775f686173682c20707265765f626c6f636b2e686173685369676e2e707269766174655f6b657929')
class GenesisProduce(Block):
    def __init__(self, dir, public_key, block_number=0, prev_hash='', private_key=None):
        super().__init__(dir, Script.PRODUCE, block_number, len(get_spendable_outputs(dir)), prev_hash)
        gladiator_hex = self.get_gladiator_hex()
        self.hashSign.add_gladiators([Gladiator([GladiatorOutput(gladiator_hex, [public_key])], [])])
        new_hash = self.do_hash()
        while not new_hash.startswith(gladiator_hex):
            self.hashSign.nonce += 1        
            if private_key: 
                self.signature = self.hashSign.add_signature(private_key)
            new_hash = self.do_hash()
        self.new_hash = new_hash
        self.save_json(dir)
    def do_hash(self):
        return sha512(pdumps(self.hashSign)).hexdigest()
    def save_json(self, dir):
        with open('./' + dir + '/block_' + str(self.hashSign.block_number) + '/jsoschon.json', 'w') as jsoschon:
            jsoschon.write(encode(self))
    # def get_block_number(self, dir):
    #     if not path.exists('./' + dir):
    #         return 0
    #     _, _, files = next(walk('./' + dir))
    #     return len(files)



class Stabbed(Block):
    def __init__(self, block_number, dir, public_keys):
        pass



class Stab(Block):
    def __int__(self, dir, public_key, prev_hash):
        _, _, files = next(walk('./' + dir))
        len_files = len(files)
        super().__init__(len_files, dir, prev_hash)
        gladiator_input = GladiatorInput()
    
    def create_attack_scripts(self, len_files, dir):
        for i in range(len_files):
            with open('./' + dir + '/block_' + str(i) + '/jsoschon.json') as jsoschon:
                block = encode(jsoschon.read())
        # later this gladiator input has to sign the stuck output
        # waarom kun je alleen maar oudere of lagere blocknummers aanvalllen omdat ik dan voor each block dat al bestaat een script kan aanmaken om aantevallen









    # def open_json():
        
    # def save_reproduce():

    # def save_produce():

    # def save_

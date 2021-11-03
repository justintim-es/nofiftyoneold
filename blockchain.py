from block import GenesisProduce
from os import path, walk
from jsonpickle import encode, decode
class Blockchain:
    def __init__(self, dir, public_key):
        self.blocks = []
        if not path.exists('./' + dir):
            self.blocks = [GenesisProduce(dir, public_key)]
        else:
            _, dirs, _ = next(walk('./' + dir)) 
            for i in range(len(dirs)):
                with open('./' + dir + '/block_' + str(i) + '/jsoschon.json') as jsoschon:
                    self.blocks.append(decode(jsoschon.read())) 
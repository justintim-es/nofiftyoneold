from block import GenesisProduce
from os import walk
from argparse import ArgumentParser
from jsonpickle import encode, decode
arg_parser = ArgumentParser()
arg_parser.add_argument('--public_key', required=True)
aschargs = arg_parser.parse_args()
_, dirs, _ = next(walk('../'))
with open('../block_' + str(len(dirs)-1) + '/jsoschon.json') as jsoschon:
    prev_block = decode(jsoschon.read())
    block = GenesisProduce('../', aschargs.public_key, len(dirs), prev_block.new_hash, prev_block.hashSign.private_key)
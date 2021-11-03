from jsonpickle import encode, decode
from socket import SOCK_STREAM, AF_INET, socket
def open_json(block_number):
    with socket(AF_INET, SOCK_STREAM) as s:
        with open('./blocks/block_' + str(block_number)  + '/jsoschon.json', 'r') as jsoschon:
            print(encode(jsoschon.read()))    
open()
   

   we need to create an inner p2p connection that gives us the blocknumber
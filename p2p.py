from socket import socket, AF_INET, SOCK_STREAM

class Handshake:
    def __init__(self, zero):
        self.zero = zero


class P2p:
    def __init__(self, internal_ip, port, blockchain, bootnode=None):
        self.internal_ip: str = internal_ip
        self.port: int = int(port)
        self.blockchain = blockchain
        if bootnode is not None:
            self.sockets = [bootnode]
        else:
            self.sockets = []
    def listen(self):
            with socket(AF_INET, SOCK_STREAM) as s:
                s.bind((self.ip, self.port))
                s.listen()
                conn, addr = s.accept()
                with conn:
                    while True:
                        data = conn.recv()
                        if not data:
                            continue
                        
    def send_blocknumber(self):
        with socket(AF_INET, SOCK_STREAM) as s:
            
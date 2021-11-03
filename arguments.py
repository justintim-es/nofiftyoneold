from argparse import ArgumentParser

class Aschargs:
    def __init__(self):    
        arg_parser = ArgumentParser()
        arg_parser.add_argument('--bootnode', required=False)
        arg_parser.add_argument('--internal_ip', required=True)
        arg_parser.add_argument('--p2p_port', required=True)
        arg_parser.add_argument('--block_dir', required=True)
        arg_parser.add_argument('--seed', required=True)
        # arg_parser.add_argument('--rpc_port', required=True)
        self.args = arg_parser.parse_args()
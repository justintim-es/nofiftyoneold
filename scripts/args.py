from argparse import ArgumentParser

arg_parser = ArgumentParser()
arg_parser.add_argument('--test')
aschargs = arg_parser.parse_args()
print(aschargs.test)
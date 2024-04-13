# Python argparse: Pass a List as command-line argument

import argparse


parser = argparse.ArgumentParser(
    description='A sample Argument Parser.'
)

parser.add_argument('-l',
                    '--list',
                    nargs='+',
                    required=True)

args = parser.parse_args()

print(args.list)
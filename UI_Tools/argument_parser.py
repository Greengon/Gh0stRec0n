"""
This file will be responsible for
handling the user arguments.
"""
import argparse  # Parser for command-line options, arguments and sub-commands.
import sys


def args_parser():
    parser = argparse.ArgumentParser(description='Ports scanner utility.', add_help=True)
    # Print the help message if no args where given
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit()

    args = parser.parse_args()
    print(args)


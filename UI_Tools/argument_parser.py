"""
This file will be responsible for
handling the user arguments.
"""
import argparse  # Parser for command-line options, arguments and sub-commands.
import sys
from TCP.tcp_client import use_tcp_client


def args_parser():
    parser = argparse.ArgumentParser(description='Ports scanner utility.', add_help=True)
    parser.add_argument("-Tc", "--tcp-client", action='store_true', help="Create a tcp client")
    # Print the help message if no args where given
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit()

    # Let's check which option the user choose
    args = parser.parse_args()
    if args.tcp_client is True:
        use_tcp_client()
    else:
        print(args)


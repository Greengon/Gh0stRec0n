"""
This file will be responsible for
handling the user arguments.
"""
import argparse  # Parser for command-line options, arguments and sub-commands.
import sys
from TCP.tcp_client import use_tcp_client
from TCP.tcp_server import use_tcp_server
from UDP.udp_client import use_udp_client


def args_parser():
    parser = argparse.ArgumentParser(description='Ports scanner utility.', add_help=True)
    # TODO: enable excepting several IPs
    parser.add_argument("IP", action='store', help="Target IP")
    parser.add_argument("-p",
                        "--port",
                        action='store',
                        nargs=1,
                        help="decide which ports you want to target",
                        type=int,
                        metavar="<port number>")
    parser.add_argument("-Tc", "--tcp-client", action='store_true', help="Create a TCP client")
    parser.add_argument("-Ud", "--udp-client", action='store_true', help="Create a UDP client")
    parser.add_argument("-TS", "--tcp-server", action='store_true', help="Create a TCP server")
    # Print the help message if no args where given
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit()

    # Let's check which option the user choose
    try:
        args = parser.parse_args()
        if args.tcp_client is True:
            use_tcp_client(args.IP, args.port[0])
        elif args.udp_client is True:
            use_udp_client(args.IP, args.port[0])
        elif args.tcp_server is True:
            use_tcp_server(args.IP, args.port[0])
        else:
            parser.print_help(sys.stderr)
            sys.exit()
    except Exception as error:
        print(error)
        sys.exit()


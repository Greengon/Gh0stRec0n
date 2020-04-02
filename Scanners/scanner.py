# This will be our host discovery scanner
import socket
import os

"""
Using UDP for scanning:
When we send UDP datagram to a closed port on a host, the
host typically send back an ICMP message indicating that the 
port is unreachable.

NOTE:
We are using promiscuous mode, which requires administrative
privileges.
Promiscuous mode allows us to sniff all packets that the network
card sees, even those not destined for your specific host.
"""


class Scanner:
    def __init__(self):
        # Host to listen on
        # self.host = socket.gethostbyname(socket.gethostname())
        self.host = "127.0.0.1"

        # create a raw socket and bind it to the public interface
        """
        The difference between Windows and Linux is that Windows
        will allow us to sniff all incoming packets regardless
        of protocol, whereas Linux forces us to specify what we are
        sniffing.
        """
        # TODO: Check for MacOS
        if os.name == "nt":
            self.socket_protocol = socket.IPPROTO_IP
        else:
            self.socket_protocol = socket.IPPROTO_ICMP

    # Simple raw socket sniffer
    def sniff(self):
        try:
            sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, self.socket_protocol)
            sniffer.bind((self.host, 0))

            # we want the IP headers included in the capture
            sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

            """
            If we're using Windows, we need to send an IOCTL
            to the network card driver to enable promiscuous mode.
            """
            if os.name == "nt":
                sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

            # read in a single packet
            print(sniffer.recvfrom(65565))

            # If we're using Windows, turn off promiscuous mode
            if os.name == "nt":
                sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
        except Exception as error:
            print(error)


def start_scanner():
    scanner = Scanner()
    scanner.sniff()

start_scanner()
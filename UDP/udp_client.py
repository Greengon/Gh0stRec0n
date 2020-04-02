# A UDP client modified for the scanner needs
import socket


class UDPClient:

    # TODO set for wrong input
    # TODO create default ports to use
    def __init__(self, ip, port):
        self.target_host = ip
        self.target_port = port

    def send(self):
        # create a socket object
        # AF_INET: use IPv4 address or hostname
        # SOCK_DGRAM: use UDP
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # send some data
        client.sendto(b'AAABBBCCC', (self.target_host, self.target_port))

        # receive some data
        # recvfrom return both data and the details of the remote host and port
        # TODO: handle server no sending back anything
        data, addr = client.recvfrom(4096)

        print(data)


def use_udp_client(ip, port):
    udp_client = UDPClient(ip, port)
    udp_client.send()

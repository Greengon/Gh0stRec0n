# A TCP client modified for the scanner needs
import socket


class TCPClient:
    # TODO set for wrong input
    def __init__(self, ip, port):
        self.target_host = ip
        self.target_port = port

    def connect(self):
        # create a socket object
        # AF_INET: use IPv4 address or hostname
        # SOCK_STREAM: use TCP
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # connect to client
        # TODO: handle failed connection.
        client.connect((self.target_host, self.target_port))

        # send some data
        # TODO: handle server sending data first.
        client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

        # receive some data
        # TODO: handle server no sending back anything
        response = client.recv(4096)

        print(response)


# usage function of this class
def use_tcp_client(ip, port):
    tcp_client = TCPClient(ip, port)
    tcp_client.connect()

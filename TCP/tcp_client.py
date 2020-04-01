# A TCP client modified for the scanner needs
import socket


class TcpClient:
    def __init__(self):
        self.target_host = "www.google.com"
        self.target_port = 80

    def connect(self):
        # create a socket object
        # AF_INET: use IPv4 address or hostname
        # SOCK_STREAM: use TCP
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # connect to client
        client.connect((self.target_host, self.target_port))

        # send some data
        client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

        # receive some data
        response = client.recv(4096)

        print(response)


# usage function of this class
def use_tcp_client():
    tcp_client = TcpClient()
    tcp_client.connect()

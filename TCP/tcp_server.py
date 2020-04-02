# This is a tcp server modified for the scanner
import socket
import threading


class TCPServer:

    # TODO set for wrong input
    # TODO create default ports to use
    def __init__(self, ip, port):
        self.bind_ip = ip
        self.bind_port = port

    # This is our client-handling thread
    def handle_client(self, client_socket):
        # print out what the client sends
        request = client_socket.recv(1024)

        print("[*] Received: %s" % request)

        # send back a packet
        client_socket.send("ACK!")

        client_socket.close()

    def awake(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # setting the ip and port to listen to
        server.bind((self.bind_ip, self.bind_port))
        # start listening with maximum backlog connection set to 5
        # TODO: get user input for max connections
        server.listen(5)

        print("[*] Listening on %s:%d" % (self.bind_ip, self.bind_port))

        while True:
            # When a client connects we get client socket and remote connection details
            client, address = server.accept()

            print("[*] Accepted connection from: %s:%d" % (address[0], address[1]))

            # spin op our client thread to handle incoming data
            client_handler = threading.Thread(target=self.handle_client, args=(client,))
            client_handler.start()


def use_tcp_server(ip, port):
    tcp_server = TCPServer(ip, port)
    tcp_server.awake()

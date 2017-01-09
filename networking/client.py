import socket

class Client:
    def __init__(self, connetion):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(connection, 612)

    def send(self, msg):
        return self.s.send((msg.encode("utf-8")))

    def receive(self, size: int):
        return self.s.recv(size)

    def receive(self, delimiter: str):
        end = False
        message = ""
        while not end:
            x = ""
            try:
                x = self.s.recv(1)
            except socket.error:
                end = True
            if x == delimiter:
                end = True
            else:
                message += x

        return message

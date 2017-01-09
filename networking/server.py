import socket

class Server:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((socket.gethostname(), 612))
        self.s.listen(5)

    def send(self, msg):
        accepted = self.s.accept()
        print "Accepted connection from: " + accepted[1]
        accepted[0].send(msg)

    def receive(self, size: int):
        accepted = self.s.accept()
        print "Accepted connection from: " + accepted[1]
        return accepted[0].recv(size)

    def receive(self, delimiter: str):
        accepted = self.s.accept()
        print "Accepted connection from: " + accepted[1]

        end = False
        message = ""
        while not end:
            x = ""
            try:
                x = accepted[0].recv(1)
            except socket.error:
                end = True
            if x == delimiter:
                end = True
            else:
                message += x

        return message'

    def end(self):
        self.s.close()

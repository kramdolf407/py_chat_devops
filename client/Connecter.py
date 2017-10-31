import socket
import _thread

server_ip = 'localhost'
server_port = 9999

class Connecter:

    def __init__(self):
        self.clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def connect(self,server_ip, server_port):
        self.clientSocket.connect((server_ip, server_port))

    def sendMsg(self,text):
        self.clientSocket.send(str.encode(text))

    def startReceiverThread(self,chattViewer_):
        self.chattViewer = chattViewer_
        _thread.start_new_thread(self.func_to_receiver,())

    def func_to_receiver(self):
        while True:
            msg = self.clientSocket.recv(1024).decode()
            self.chattViewer.showMessage(msg)

    def connect_conf(self, ip, port):
        global server_ip
        global server_port

        server_ip = ip
        server_port = port
        self.clientSocket.connect((server_ip, server_port))

# Not finished
class ConnecterConf:

    def connect_conf(ip, port):
        global server_ip
        global server_port
        self = Connecter
        server_ip = ip
        server_port = port
        Connecter.connect(self, server_ip, server_port)

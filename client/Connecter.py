import socket
import _thread

class Connecter:

    def __init__(self):
        self.clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# TODO: Add try and except ("ConnectionRefusedErrror", "TimeoutErrror")
    def connect(self,server_ip, server_port):
        self.clientSocket.connect((server_ip, server_port))

    def sendMsg(self, text):
        self.clientSocket.send(str.encode(text))

    def startReceiverThread(self,chattViewer_):
        self.chattViewer = chattViewer_
        _thread.start_new_thread(self.func_to_receiver,())

    def func_to_receiver(self):
        while True:
            msg = self.clientSocket.recv(1024).decode()
            self.chattViewer.showMessage(msg)

    def connect_ip(serverip):
        global server_ip
        server_ip = serverip
        print(server_ip)

    def connect_port(serverport):
        global server_port
        server_port = serverport
        print(server_port)

    def connect_conf(self):
        global server_ip
        global server_port
        Connecter.connect(self, str(server_ip), int(server_port))



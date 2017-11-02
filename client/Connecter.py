import socket
import _thread

class Connecter:

    def __init__(self):
        self.clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def connect_ip(serverip):
        global server_ip
        server_ip = serverip

    def connect_port(serverport):
        global server_port
        server_port = serverport

    def connect_conf(self):
        global server_ip
        global server_port
        Connecter.connect(self, str(server_ip), int(server_port))

# TODO: Add try and except ("ConnectionRefusedErrror", "TimeoutErrror")
    def connect(self,server_ip, server_port):
        try:
            self.clientSocket.connect((server_ip, server_port))
        except ConnectionRefusedError:
            print("ConnectionRefueseDerrrororo")
            return False

        except TimeoutError:
            print("TimeoutErrro")
            return False

    def sendMsg(self, text):
        try:
            self.clientSocket.send(str.encode(text))
        except OSError:
            return False

    def startReceiverThread(self,chattViewer_):
        self.chattViewer = chattViewer_
        _thread.start_new_thread(self.func_to_receiver,())

    def func_to_receiver(self):
        while True:
            msg = self.clientSocket.recv(1024).decode()
            self.chattViewer.showMessage(msg)








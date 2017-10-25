import socket
import _thread

class Connecter:
    def __init__(self):
        self.clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def connect(self,ip, port):
        self.clientSocket.connect((ip,port))

    def sendMsg(self,text):
        self.clientSocket.send(str.encode(text))

    def startReceiverThread(self,chattViewer_):
        self.chattViewer = chattViewer_
        _thread.start_new_thread(self.func_to_receiver,())

    def func_to_receiver(self):
        while True:
            msg = self.clientSocket.recv(1024).decode()
            self.chattViewer.showMessage(msg)

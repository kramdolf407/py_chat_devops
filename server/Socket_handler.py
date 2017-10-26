import socket
import _thread

#test
class Socket_handler:
    def __init__(self):
        self.serverSocket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.serverSocket.bind(('',9999))
        self.serverSocket.listen()
        self.list_of_sockets = []

    def init_the_view_obj(self,chattViewer_):
        self.chattViewer = chattViewer_

    def acceptConnection(self):
        clientSocket, addr = self.serverSocket.accept()
        self.list_of_sockets.append(clientSocket)

        self.startReceiver(clientSocket)

        #starta recev

    def sendMsg(self,text):
        for soc in self.list_of_sockets:
            soc.send(str.encode(text))

    def startReceiver(self, csock):
        _thread.start_new_thread(self.func_to_receiver,(csock,))

    def func_to_receiver(self,csock):
        while True:
            for csock in self.list_of_sockets:
                msg = csock.recv(1024).decode()
                self.chattViewer.showMessage(msg)
                csock.send(str.encode(msg))

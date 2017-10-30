import socket
import _thread

class Socket_handler:

    def __init__(self):
        self.serverSocket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.serverSocket.bind(('localhost',int(server_port)))
        self.serverSocket.listen()
        self.list_of_sockets = []
        self.list_of_addr = []
        #self.list_of_users = []
        #self.read_file_of_users()

    def init_the_view_obj(self,chattViewer_):
        self.chattViewer = chattViewer_

    def acceptConnection(self):
        clientSocket, addr = self.serverSocket.accept()
        self.list_of_addr.append(addr)
        self.list_of_sockets.append(clientSocket)

        self.startReceiver(clientSocket, addr)

    def sendMsg(self,text):
        self.chattViewer.showMessage("Admin: "+text)
        for soc in self.list_of_sockets:
            soc.send(str.encode("Admin: "+text))

    def startReceiver(self, csock, addr):
        _thread.start_new_thread(self.func_to_receiver,(csock,addr,))

    def func_to_receiver(self,csock, addr):
        while True:
            msg = csock.recv(1024).decode()
            self.chattViewer.showMessage(str(addr)+": "+msg)
            for sock in self.list_of_sockets:
                sock.send(str.encode(str(addr)+": "+msg))

    def server_port(srvport):
        global server_port
        server_port = srvport
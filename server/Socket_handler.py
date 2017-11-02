import socket
import _thread

server_port = 9999


class Socket_handler:

    def __init__(self):
        try:
            self.serverSocket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.serverSocket.bind(('localhost',int(server_port)))
            self.serverSocket.listen()
            self.list_of_sockets = []
            self.list_of_addr = []

# TODO , throws error if port already in use. BUT needs to return back to startUp, not continues
        except OSError:
            print("Port already in use!!")
            return

    def init_the_view_obj(self,chattViewer_):
        self.chattViewer = chattViewer_

    def acceptConnection(self):
        clientSocket, addr = self.serverSocket.accept()
        self.list_of_addr.append(addr)
        self.list_of_sockets.append(clientSocket)
        self.startReceiver(clientSocket, addr)


# TODO add try and except (ConnectionResetError):
    def sendMsg(self,text):
        try:
            self.chattViewer.showMessage("Admin: "+text)
            for soc in self.list_of_sockets:
                try:
                    soc.send(str.encode("Admin: "+text))
                except Exception:
                    soc.close()
                    self.list_of_sockets.remove(soc)

        except ConnectionResetError:
            print("ConnectionResetError in sendMSG")

    def startReceiver(self, csock, addr):
        _thread.start_new_thread(self.func_to_receiver,(csock,addr,))

    def func_to_receiver(self,csock, addr):
        while True:
            try:
                msg = csock.recv(1024).decode()
                if not msg == "":
                    self.chattViewer.showMessage(str(addr)+ " " + msg)
                    for sock in self.list_of_sockets:#
                        sock.send(str.encode(str(addr)+ ": " + msg))
            except OSError:
                print(csock)
                csock.close()
                return False



    def server_port(srvport):
        global server_port
        server_port = srvport
from server.ChattViewer import ChattStartup , ChattViewer
from server.Socket_handler import Socket_handler
import _thread

ChattStartup()

sock_handler = Socket_handler()

chattV = ChattViewer(sock_handler)

chattV.buildGui()

sock_handler.init_the_view_obj(chattV)

def funcToThread():
    while True:
        sock_handler.acceptConnection()

_thread.start_new_thread(funcToThread, ())

chattV.start()



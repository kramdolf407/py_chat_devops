from client.ChattViewer import ChattViewer
from client.Connecter import Connecter

connecter = Connecter()
connecter.connect('127.0.0.1',9999)

chattV = ChattViewer(connecter)
chattV.buildGui()

connecter.startReceiverThread(chattV)
chattV.start()
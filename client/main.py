from client.ChattViewer import ChattStartup, ChattViewer
from client.Connecter import Connecter

ChattStartup()

connecter = Connecter()
connecter.connect('localhost',9999)

chattV = ChattViewer(connecter)
chattV.buildGui()

connecter.startReceiverThread(chattV)
chattV.start()
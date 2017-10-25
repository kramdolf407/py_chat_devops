import tkinter

class ChattViewer:
    def __init__(self,connecter_):
        self.connecter = connecter_
        self.root = tkinter.Tk()

    def buildGui(self):

        #we build the chattContent
        scroll = tkinter.Scrollbar(self.root)
        scroll.grid(row = 0, column = 1, sticky=tkinter.N+tkinter.S)

        self.chattContents = tkinter.Text(self.root, yscrollcommand  = scroll.set)
        self.chattContents.configure(state="disabled")
        self.chattContents.grid(row = 0,column = 0)

        scroll.config(command=self.chattContents.yview)

        #we build the Enry
        self.entryOfUser = tkinter.Entry(self.root)
        self.entryOfUser.grid(row = 1,column = 0)

        #we build the button
        self.buttonToTrigg = tkinter.Button(self.root, text = "enter", command = self.sendMsgToConnecter)
        self.buttonToTrigg.grid(row = 1,column = 1)

    def sendMsgToConnecter(self):
        self.connecter.sendMsg(self.entryOfUser.get())

    def start(self):
        self.root.mainloop()

    def showMessage(self,text):
        self.chattContents.insert(tkinter.END,text+"\n")

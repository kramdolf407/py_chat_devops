import tkinter
from tkinter import messagebox

started = False

class ChattStartup():

        def __init__(self):
            super().__init__()
            self.root = tkinter.Tk()
            self.label = None
            self.entry = None
            self.button = None
            self.srvport= None
            self.srvmaxcon = None
            self.build_window()
            self.run()

        def build_window(self):

            self.label_srvmaxcon = tkinter.Label(self.root, text='Max connections: ', width=20)
            self.label_srvport = tkinter.Label(self.root, text='Port: ', width=20)

            self.label_srvmaxcon.grid(row=0, column=0)
            self.label_srvport.grid(row=1, column=0)

            self.entry_srvmaxcon = tkinter.Entry(self.root, width=20)
            self.entry_srvmaxcon.focus_set()
            self.entry_srvmaxcon.grid(row=0, column=1)

            self.entry_srvport = tkinter.Entry(self.root, width=20)
            self.entry_srvport.focus_set()
            self.entry_srvport.grid(row=1, column=1)

            self.button_login = tkinter.Button(self.root, text='Host channel')
            self.button_login.grid(row=2, column=0)
            self.button_login.bind('<Button-1>', self.get_srv_conf)

        def run(self):
            self.root.mainloop()
            self.root.destroy()

        def get_srv_conf(self, event):
            self.srvmaxcon = self.entry_srvmaxcon.get()
            self.srvport = self.entry_srvport.get()
            self.root.quit()


class ChattViewer():

    def __init__(self,listener_, master=None):
        super(ChattViewer, self).__init__()
        self.listener = listener_
        self.root = tkinter.Tk()
        self.root.title('Server Chat')


    def start(self):
        self.root.mainloop()
        self.root.destroy()

    def buildGui(self, master=None):
        global started
        #we build the chattContent
        started = True
        scroll = tkinter.Scrollbar(self.root)
        scroll.grid(row = 0, column = 1, sticky=tkinter.N+tkinter.S)

        self.chattContents = tkinter.Text(self.root, yscrollcommand  = scroll.set)
        #self.chattContents.configure(state="disabled")

        self.chattContents.grid(row = 0,column = 0)

        scroll.config(command=self.chattContents.yview)

        #we build the Enry
        self.entryOfUser = tkinter.Entry(self.root)
        self.entryOfUser.grid(row = 1,column = 0)

        #we build the button
        self.buttonToTrigg = tkinter.Button(self.root, text = "enter", command = self.sendMsgToListener)
        self.buttonToTrigg.grid(row = 1,column = 1)

        # master.bind('<Return>', self.sendMsgToListener)

    def sendMsgToListener(self):
        self.listener.sendMsg(self.entryOfUser.get())



    def showMessage(self,text):
        self.chattContents.insert(tkinter.END,text+"\n")

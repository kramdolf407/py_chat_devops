import tkinter
from tkinter import messagebox
from server.Socket_handler import *

started = False

class ChattStartup():

        def __init__(self):
            self.root = tkinter.Tk()
            self.entry_srvport = None
            self.build_window()
            self.run()

        def build_window(self):

            self.label_srvport = tkinter.Label(self.root, text='Port (999-65535): ', width=20)
            self.label_srvport.grid(row=1, column=0)

            self.entry_srvport = tkinter.Entry(self.root, width=20)
            self.entry_srvport.focus_set()
            self.entry_srvport.grid(row=1, column=1)

            self.button_login = tkinter.Button(self.root, text='Host channel')
            self.button_login.grid(row=2, column=0)
            self.button_login.bind('<Button-1>', self.server_config_start)

        def run(self):
            self.root.mainloop()
            self.root.destroy()

        def server_config_start(self, new_port):
            new_port = self.entry_srvport.get()
            if not self.port_validate(new_port):
                tkinter.messagebox.showinfo('Port invalid', 'You can only choose one port from 999 to 65535')
                return
            else:
                Socket_handler.server_port(new_port)
                self.root.quit()
                return

        def port_validate(self, new_port):
            try:
                new_port = int(new_port)
                if new_port > 999 and new_port <= 65535:
                    return True
                return False
            except:
                return False

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
        self.buttonToTrigg = tkinter.Button(self.root, text = "Send", bg='red', bd=3, command = self.sendMsgToListener)
        self.buttonToTrigg.grid(row = 1,column = 1)

        # master.bind('<Return>', self.sendMsgToListener)

    def sendMsgToListener(self):
        self.listener.sendMsg(self.entryOfUser.get())

    def showMessage(self,text):
        self.chattContents.insert(tkinter.END,text+"\n")

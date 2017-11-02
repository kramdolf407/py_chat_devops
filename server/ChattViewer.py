import tkinter
from tkinter import messagebox
from tkinter import Menu
from server.Socket_handler import *


class ChattStartup():

        def __init__(self):
            self.root = tkinter.Tk()
            self.root.title('Host configurator')
            self.build_window()
            self.run()

        def build_window(self):

            self.label_srvport = tkinter.Label(self.root, text='Port (1000-65535): ', width=20)
            self.label_srvport.grid(row=1, column=0)

            self.entry_srvport = tkinter.Entry(self.root, width=20)
            self.entry_srvport.focus_set()
            self.entry_srvport.grid(row=1, column=1)

            self.button_login = tkinter.Button(self.root, text='Host channel', bg='chartreuse3')
            self.button_login.grid(row=2, column=1)
            self.button_login.bind('<Button-1>', self.server_config_start)

        def run(self):
            self.root.mainloop()
            self.root.destroy()

        def server_config_start(self, new_port):
            new_port = self.entry_srvport.get()
            if not self.port_validate(new_port):
                tkinter.messagebox.showinfo('Port invalid', 'You can only choose one port from 1000 to 65535')
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

        menuBar=Menu(self.root)
        self.root.config(menu=menuBar)
        fileMenu = Menu(menuBar, tearoff=0)
        fileMenu.add_command(label="Kick user", command=self.kick_user)
        fileMenu.add_separator()
        fileMenu.add_command(label="List of users", command=self.list_users)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self.quit_me)
        menuBar.add_cascade(label="Commands", menu=fileMenu)

        #we build the chattContent
        scroll = tkinter.Scrollbar(self.root)
        scroll.grid(row = 0, column = 1, sticky=tkinter.N+tkinter.S)

        self.chattContents = tkinter.Text(self.root, yscrollcommand  = scroll.set)
        self.chattContents.configure(state="disabled")

        self.chattContents.grid(row = 0,column = 0)

        scroll.config(command=self.chattContents.yview)

        #we build the Enry
        self.entryOfUser = tkinter.Entry(self.root, width=90)
        self.entryOfUser.grid(row = 1,column = 0)

        #we build the button
        self.buttonToTrigg = tkinter.Button(self.root, text = "Send", bg='IndianRed1', bd=3, command = self.sendMsgToListener)
        self.buttonToTrigg.grid(row = 1,column = 1)

        # master.bind('<Return>', self.sendMsgToListener)

    def sendMsgToListener(self):
        self.listener.sendMsg(self.entryOfUser.get())

    def showMessage(self,text):
        self.chattContents.configure(state="normal")
        self.chattContents.insert(tkinter.END,text+"\n")
        self.chattContents.configure(state="disabled")
# TODO COMPLETE:
    def kick_user(self):
        print("Kick user")

    def list_users(self):
        print("I want to list users")

    def quit_me(self):
        self.root.quit()
        self.root.destroy()
        exit()
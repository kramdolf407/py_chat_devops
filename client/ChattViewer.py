import tkinter


class ChattStartup():
    def __init__(self):
        super().__init__()
        self.root = tkinter.Tk()
        self.label = None
        self.entry = None
        self.button = None
        self.login = None

        self.build_window()
        self.run()

    def build_window(self):

        self.label_srvip = tkinter.Label(self.root, text='Host IP: ', width=20)
        self.label_srvport = tkinter.Label(self.root, text='Host port: ', width=20)
        self.label_username = tkinter.Label(self.root, text='Your username: ', width=20)
        self.label_password = tkinter.Label(self.root, text='Password: ', width=20)

        self.label_srvip.grid(row=0,column=0)
        self.label_srvport.grid(row=1,column=0)
        self.label_username.grid(row=2,column=0)
        self.label_password.grid(row=3,column=0)

        self.entry_srvip = tkinter.Entry(self.root, width=20)
        self.entry_srvip.focus_set()
        self.entry_srvip.grid(row=0,column=1)

        self.entry_srvport = tkinter.Entry(self.root, width=20)
        self.entry_srvport.focus_set()
        self.entry_srvport.grid(row=1,column=1)

        self.entry_username = tkinter.Entry(self.root, width=20)
        self.entry_username.focus_set()
        self.entry_username.grid(row=2,column=1)
        self.entry_username.bind('<Return>', self.get_login_event)

        self.entry_password = tkinter.Entry(self.root, width=20)
        self.entry_password.focus_set()
        self.entry_password.grid(row=3,column=1)


        self.button_login = tkinter.Button(self.root, text='Login')
        self.button_register = tkinter.Button(self.root, text='Register New')
        self.button_login.grid(row=4, column=0)
        self.button_register.grid(row=4, column=1)
        self.button_register.bind('<Button-1>', self.get_login_event)

    def run(self):
        self.root.mainloop()
        self.root.destroy()

    def get_login_event(self, event):
        self.username= self.entry_username.get()
        self.password = self.entry_password.get()
        self.root.quit()


class ChattViewer:
    def __init__(self,connecter_):
        self.connecter = connecter_
        self.root = tkinter.Tk()
        self.root.title('Client Chat')

    def buildGui(self, master=None):

        #we build the chattContent/
        scroll = tkinter.Scrollbar(self.root)
        scroll.grid(row = 0, column = 1, sticky=tkinter.N+tkinter.S)

        self.chattContents = tkinter.Text(self.root, yscrollcommand  = scroll.set)
# Uncomment later. When sending messages , change state=disabled
        #self.chattContents.configure(state="disabled")
        self.chattContents.grid(row = 0,column = 0)

        scroll.config(command=self.chattContents.yview)

        #we build the Enry
        self.entryOfUser = tkinter.Entry(self.root)
        self.entryOfUser.grid(row = 1,column = 0)

        #we build the button
        self.buttonToTrigg = tkinter.Button(self.root, text = "enter", command = self.sendMsgToConnecter)
        self.buttonToTrigg.grid(row = 1,column = 1)

        self.buttonToTrigg.bind('<Return>', self.sendMsgToConnecter)

    def sendMsgToConnecter(self):
        self.connecter.sendMsg(self.entryOfUser.get())

    def start(self):
        self.root.mainloop()

    def showMessage(self,text):
        self.chattContents.insert(tkinter.END,text+"\n")

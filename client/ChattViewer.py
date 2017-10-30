import tkinter
import tkinter.messagebox
from client.user_class import *
from client.Connecter import *


class ChattStartup():
    def __init__(self):
        self.root = tkinter.Tk()
        self.entry_srvip = None
        self.entry_srvport = None
        self.entry_username = None
        self.entry_password = None
        self.entry_email = None
        self.entry_nickname = None
        self.test_obj = Collection_of_users()

        self.build_window()
        self.run()

    def build_window(self):

        self.label_srvip = tkinter.Label(self.root, text='Connect to IP: ', width=20)
        self.label_srvport = tkinter.Label(self.root, text='Connect to port: ', width=20)

        self.label_username = tkinter.Label(self.root, text='Your username: ', width=20)
        self.label_password = tkinter.Label(self.root, text='Password: ', width=20)
        self.label_email = tkinter.Label(self.root, text='Email: ', width=20)
        self.label_nickname = tkinter.Label(self.root, text='Nickname: ', width=20)
        # Grid buttons
        self.label_srvip.grid(row=0,column=0)
        self.label_srvport.grid(row=1,column=0)
        self.label_username.grid(row=2,column=0)
        self.label_password.grid(row=3,column=0)
        self.label_email.grid(row=4,column=0)
        self.label_nickname.grid(row=5,column=0)
        # Grid entries, set focus and bind keys:
        self.entry_srvip = tkinter.Entry(self.root, width=20)
        self.entry_srvip.focus_set()
        self.entry_srvip.grid(row=0,column=1)

        self.entry_srvport = tkinter.Entry(self.root, width=20)
        self.entry_srvport.focus_set()
        self.entry_srvport.grid(row=1,column=1)

        self.entry_username = tkinter.Entry(self.root, width=20)
        self.entry_username.focus_set()
        self.entry_username.grid(row=2,column=1)
        self.entry_username.bind(self.get_login_event)

        self.entry_password = tkinter.Entry(self.root, width=20)
        self.entry_password.grid(row=3,column=1)
        self.entry_password.bind(self.get_login_event)

        self.entry_email = tkinter.Entry(self.root, width=20)
        self.entry_email.grid(row=4, column=1)
        self.entry_email.bind(self.get_login_event)

        self.entry_nickname = tkinter.Entry(self.root, width=20)
        self.entry_nickname.grid(row=5, column=1)
        self.entry_nickname.bind(self.get_login_event)

        self.button_login = tkinter.Button(self.root, text='Login')
        self.button_register = tkinter.Button(self.root, text='Register New')
        self.button_login.grid(row=6, column=0)
        self.button_register.grid(row=6, column=1)
        self.button_login.bind('<Button-1>', self.get_login_event)
        self.button_register.bind('<Button-1>', self.get_login_event)

    def run(self):
        self.root.mainloop()
        self.root.destroy()
# Bind to login
    def get_login_event(self, event):
        self.username_login = self.entry_username.get()
        self.password_login = self.entry_password.get()
        self.email_login = self.entry_email.get()
        self.nickname_login = self.entry_nickname.get()
        self.root.quit()

# Bind to register
    def get_register_event(self, event):

        self.username_register = self.entry_username.get()
        self.userpass_register = self.entry_password.get()
        self.email_login = self.entry_email.get()
        self.nickname_login = self.nickname_login.get()
        self.userip_connect = self.entry_srvip.get()
        self.userport_connect = self.entry_srvport.get()
        self.test_obj.add_new(self.username_register, self.userpass_register, self.email_login, self.nickname_login)
        User.is_this_user(self.username_register, self.userpass_register)
        self.root.quit()


# EDIT ------------
    def client_connect(self, ip, port):

        port = self.entry_srvport.get()
        ip = self.entry_srvip.get()
        if not self.port_validate(port):
            tkinter.messagebox.showinfo('Port invalid', 'You can only choose one port from 999 to 65535')
            return
        else:
            Connecter.connect_conf(ip, port)
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
# --------------------

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
        self.buttonToTrigg.bind('<Return>', self.sendMsgToConnecter())
        self.buttonToTrigg.grid(row = 1,column = 1)


    def sendMsgToConnecter(self):
        self.connecter.sendMsg(self.entryOfUser.get())

    def start(self):
        self.root.mainloop()

    def showMessage(self,text):
        self.chattContents.insert(tkinter.END,text+"\n")

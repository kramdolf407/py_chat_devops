class User:

    def __init__(self, username_, password_):
        #self.id = id_
        self.username = username_
        self.password = password_
        #self.email = email_

    def toString(self):
        return_string = (" | Username: "+ self.username + " | Password: "+ self.password)
        return return_string

class Login_user:

    def __init__(self, username_, password_):
        self.username = username_
        self.password = password_
        self.users = []
        self.passwords = []

    def register_user(self, username, password):

        try:
            file = open("users.txt", "a")
            file.write(username+"\n")
            file.write(password+"\n")
            file.write("\n")
            file.close()
            return True
        except:
            return False




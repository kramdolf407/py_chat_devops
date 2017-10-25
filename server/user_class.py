
class User:

    def __init__(self,id_, username_, email_, password_):
        self.id = id_
        self.username = username_
        self.password = password_
        self.email = email_

    def toString(self):
        return_string = "ID: " + str(self.id) + " | Username: "+ self.username + " | Password: "+ self.password + " | Email: "+ self.email
        return return_string
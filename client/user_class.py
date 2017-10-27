class User:

    def __init__(self, username_, password_, email_, name_):
        #self.id = id_
        self.username = username_
        self.password = password_
        self.email = email_
        self.name = name_

    def is_this_user(self, username, password):
        if (username == self.username and password == self.password):
            return True
        else:
            return False

class Collection_of_users:
    def __init__(self):
        self.list_of_users = []

    def add_new(self, username, password, email, name):
        user1 = User(username, password, email, name)
        self.list_of_users.append(user1)

    def log_in(self, username, password):
        for user in self.list_of_users:
            if (user.is_this_user(username, password) == True):
                return "Login succeed"

        return "Login failed"

    def write_users_to_file(self):

        file = open("users.txt", "a")
        for user in self.list_of_users:

            file.write(username+"\n")
            file.write(password+"\n")
            file.write(email+"\n")
            file.write(name+"\n")
            file.write("\n")
            file.close()


    def read_file_of_users(self):
        try:
            file = open("users.txt", "r")
            while True:
                user = file.readline().rstrip()
                if user == "":
                    return True

                password = file.readline().rstrip()
                if password == "":
                    return False

                email = file.readline().rstrip()
                if email == "":
                    return False

                name = file.readline().rstrip()
                if name == "":
                    return False

                file.readline()

                user1 = User(user, password, email, name)
                self.list_of_users.append(user1)
        except:
            return False
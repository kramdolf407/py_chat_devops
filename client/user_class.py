import tkinter.messagebox as msg

class User:

    def __init__(self, username_, password_, email_, name_):
        #self.id = id_
        self.username = username_
        self.password = password_
        self.email = email_
        self.name = name_

    def does_name_exist(self, username):
        print("In does_name_exist")
        if username == self.username:
            return True
        else:
            return False

    def does_user_exist(self, username, password):
        print("In does_user_exist")
        if username == self.username and password == self.password:
            return True
        else:
            return False

class Collection_of_users:

    def __init__(self):
        self.list_of_users = []

    def is_name_available(self, username):
        print("In add_new_does_name_exist")
        for user in self.list_of_users:
            if user.does_name_exist(username) == True:
                print("user already exist!")
                return False
        print("username is not in use!")

    # Ask for confirm
    # Send to ADD_NEW?
        return True

# Bind to Register
    def add_new(self, username, password, email, name):
        print("In add_new")
        user1 = User(username, password, email, name)
        self.list_of_users.append(user1)

# Bind to Login
    def log_in(self, username, password):
        print("In log_in")
        for user in self.list_of_users:
            if user.does_user_exist(username, password) == True:
                return True

        return False
#test
    def write_users_to_file(self):
        print("In write_users_to_file")
        file = open("users.txt", "w")
        for user in self.list_of_users:
            username = user.username
            password = user.password
            email = user.email
            name = user.name

            file.write(username+"\n")
            file.write(password+"\n")
            file.write(email+"\n")
            file.write(name+"\n")
            file.write("\n")
        file.close()

    def read_file_of_users(self):
        print("In read_file_of_users")
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


#list1 = Collection_of_users()
#list1.add_new("peter", "passwd", "peter@mail", "Peter")
#list1.add_new("Sara", "passwd2", "sara@mail", "Sara")
#list1.write_users_to_file()
#list1.read_file_of_users()
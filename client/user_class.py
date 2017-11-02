class User:

    def __init__(self, username_, password_, email_, name_):
        #self.id = id_
        self.username = username_
        self.password = password_
        self.email = email_
        self.name = name_

    def does_name_exist(self, username):
        if username == self.username.lower():
            return username
        else:
            return False

    def does_user_exist(self, username, password):
        if username == self.username and password == self.password:
            return True
        else:
            return False


class Collection_of_users:

    def __init__(self):
        self.list_of_users = []

    def is_name_available(self, username):
        for user in self.list_of_users:
            if user.does_name_exist(username) == True:
                print("user already exist!")
                return username
        else:
            return True

    def log_in(self, username, password):
        for user in self.list_of_users:
            if user.does_user_exist(username, password) == True:
                return True
        return False

    def add_new(self, username, password, email, name):
        user1 = User(username, password, email, name)
        self.list_of_users.append(user1)


    def delete_my_user(self, username):
        for user in self.list_of_users:
            if user.username == username:
                user.remove()

    def change_my_nicknam(self, username, new_nickname):
        for user in self.list_of_users:
            if user.username ==username:
                user.name = new_nickname

    def write_users_to_file(self):
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
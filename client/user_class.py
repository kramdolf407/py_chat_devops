class User:

    def __init__(self, username_, password_, email_, nickname_):
        #self.id = id_
        self.username = username_
        self.password = password_
        self.email = email_
        self.nickname = nickname_

    def is_this_user(self, username, password):
        if (username == self.username and password == self.password):
            return True
        else:
            return False

class Collection_of_users:
    def __init__(self):
        self.list_of_users = []

    def add_new(self, username, password, email, nickname):
        user1 = User(username, password, email, nickname)
        self.list_of_users.append(user1)

    def log_in(self, username, password):
        for user in self.list_of_users:
            if (user.is_this_user(username, password) == True):
                return "Login succeed"

        return "Login failed"
#test
    def write_users_to_file(self):

        file = open("users.txt", "a")
        for user in self.list_of_users:
            username = user.username
            password = user.password
            email = user.email
            nickname = user.nickname

            file.write(username+"\n")
            file.write(password+"\n")
            file.write(email+"\n")
            file.write(nickname+"\n")
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

                nickname = file.readline().rstrip()
                if nickname == "":
                    return False

                file.readline()

                user1 = User(user, password, email, nickname)
                self.list_of_users.append(user1)
        except:
            return False

#list1 = Collection_of_users()
#list1.add_new("peter", "passwd", "peter@mail", "Peter")
#list1.add_new("Sara", "passwd2", "sara@mail", "Sara")
#list1.write_users_to_file()
#list1.read_file_of_users()
#print(list1.list_of_users[0].username)
#print(list1.list_of_users[0].email)
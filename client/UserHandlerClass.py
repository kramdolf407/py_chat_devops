class UserHandler:
    def __init__(self, filename):
        self.list_of_users = []
        self.filename = filename

    def get_user_by_username(self, username):
        for user in self.list_of_users:
            if user.username == username.lower():
                return user
        else:
            return -1

    def add_user(self, username, password, full_name, birthday, email):
        user = self.get_user_by_username(str(username).lower())
        if user == -1:
            new_user = User(username.lower(), password, full_name, birthday, email)
            self.list_of_users.append(new_user)
            self.save_file()
            return True
        else:
            return False

    def delete_user(self, username):
        user = self.get_user_by_username(username.lower())
        if user == -1:
            return False
        else:
            self.list_of_users.remove(user)
            self.save_file()
            return True

    def to_string(self):
        return_list = []
        for user in self.list_of_users:
            return_list.append(user.to_string() + "\n\n")
        return "".join(return_list)

    def save_file(self):
        with open(self.filename + ".txt", "w") as file:
            file.write(self.to_string())

    def open_file(self):
        with open(self.filename + ".txt", "r") as file:
            while True:
                username = file.readline().rstrip("\n")
                if username == "":
                    break
                password = file.readline().rstrip("\n")
                full_name = file.readline().rstrip("\n")
                birthday = file.readline().rstrip("\n")
                email = file.readline().rstrip("\n")

                file.readline()
                new_user = User(username, password, full_name, birthday, email)
                self.list_of_users.append(new_user)

    def update_user(self, user, password, full_name, birthday, email):
        try:
            password = str(password)
            full_name = str(full_name)
            birthday = int(birthday)
            email = str(email)
        except ValueError:
            return False
        user.password = password
        user.full_name = full_name
        user.birthday = birthday
        user.email = email
        self.save_file()
        return True

    def login_user(self, username, password):
        user = self.get_user_by_username(username.lower())
        if user == -1:
            return False
        if user.password == password and user.login == 0:
            user.login_user()
            return True
        else:
            return False

    def logout_user(self, username):
        user = self.get_user_by_username(username.lower())
        if user == -1:
            return False
        else:
            user.logout_user()
            return True


class User:

    def __init__(self, username, password, full_name, birth_day, email):
        self.username = username.lower()
        self.password = password
        self.full_name = full_name
        self.birthday = birth_day
        self.email = email
        self.login = 0

    def info_string(self):
        return_string = self.full_name + ", " + str(self.birthday) + ", " + self.email
        return return_string

    def to_string(self):
        return_string = self.username + "\n" + self.password + "\n" \
                        + self.full_name + "\n" + str(self.birthday) + "\n" + self.email
        return return_string

    def login_user(self):
        self.login = 1

    def logout_user(self):
        self.login = 0

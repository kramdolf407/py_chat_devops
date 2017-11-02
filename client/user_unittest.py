from client.user_class import User
from client.user_class import Collection_of_users
import unittest

#User1 = User("peter", "abc123", "peter@mail", "P")
#User2 = User("Bill", "passwd", "bill@mail", "B")

class Tester(unittest.TestCase):

    def setup(self):
        self.test_obj = Collection_of_users()
        self.test_obj.read_file_of_users()
        print(self.test_obj[0].username)

    def test_name(self):
        name_to_test = self.test_obj[0].username
        self.assertEqual(name_to_test, "a", msg="username does not match")

    def test_passwd(self):
        passwd_to_test = self.test_obj[0].password
        self.assertEqual(passwd_to_test, "a", msg="Password do not match")


if __name__ == '__main__':
    unittest.main()
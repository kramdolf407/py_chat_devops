import unittest
from UserHandlerClass import UserHandler


class TestUserHandler(unittest.TestCase):

    def setUp(self):
        self.handler = UserHandler("testcase")
        self.handler.open_file()

    def test_add_new_user(self):
        self.assertTrue(self.handler.add_user("deckre", "deckre", "Cecilia Onselius", 19880702, "cecilia@onselius.com"))
        self.assertFalse(self.handler.add_user("larsch", "lasseman", "Lars Onselius", 19850530, "lars.onselius@telia.com"))

    def test_delete_user(self):
        self.assertFalse(self.handler.delete_user("Dallassallad"))
        self.assertTrue(self.handler.delete_user("deckre"))

    def test_update_user(self):
        user = self.handler.get_user_by_username("Larsch")
        self.handler.update_user(user, "testtest", "Lasse B", 19850531, "lasse.onselius@telia.com")

        self.assertTrue(user.password == "testtest")
        self.assertTrue(user.full_name == "Lasse B")
        self.assertTrue(user.birthday == 19850531)
        self.assertTrue(user.email == "lasse.onselius@telia.com")

        self.assertRaises(TypeError, self.handler.update_user(user, "testar", "Lasse Bertil", "ABCD", "lars@onselius.com"))

    def test_login_user(self):
        self.assertTrue(self.handler.login_user("test", "testcase"))
        self.assertFalse(self.handler.login_user("testcase", "testcase"))


if __name__ is "__main__":
    unittest.main()

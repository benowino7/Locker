import unittest
from user import User


class TestUser(unittest.TestCase):
    """ class that defines test cases"""

    def setUp(self):
        """ runs before each test case and check if the class has been instantiated correctly"""
        self.new_user = User("NewUser", "12345")

    def test_init(self):
        """Test to ensure object's initialized"""
        self.assertEqual(self.new_user.user_name, "NewUser")
        self.assertEqual(self.new_user.password, "12345")

    def test_save_user(self):
        """tests if a user credentials is successfully saved"""
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)


if __name__ == '__main__':
    unittest.main()

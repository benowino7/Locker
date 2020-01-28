import unittest
from credentials import Credentials


class TestCredentials(unittest.TestCase):
    """ Class that defines test cases
    """

    def setUp(self):
        """Set method running befor before each test case"""
        self.new_credentials = Credentials("Instagram", "345678")

    def test_credentials_instance(self):
        """Method testing whether the new_credentials have been correctly instantiated """
        self.assertEqual(self.new_credentials.account_name, "Instagram")
        self.assertEqual(self.new_credentials.account_password, "34578")

    def test_save_credentials(self):
        """tests whether the new credential created is saved"""
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_save_multiple_credentials(self):
        """saves multiple credentials to credentials_list"""
        self.new_credentials.save_credentials()
        new_test_credential = Credentials("Twitter", "86719")
        new_test_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)

    def tearDown(self):
        """ clears the credentials_list after every test hence no error"""
        Credentials.credentials_list = []

    def test_find_credential_by_name(self):
        """check if it can find credentials and display its info"""
        self.new_credentials.save_credentials()
        new_test_credential = Credentials("Twitter", "86719")
        new_test_credential.save_credentials()

        found_credential = Credentials.find_by_name("Twitter")

        self.assertEqual(found_credential.account_name, new_test_credential.account_name)

    def test_display_all_credentials(self):
        """ test if all contacts can be displayed"""
        self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)


if __name__ == '__main__':
    unittest.main()

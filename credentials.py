class Credentials:
    """Create credentials  class"""

    def __init__(self, account_name, account_password):
        self.account_name = account_name
        self.account_password = account_password

    credentials_list = []

    def save_credentials(self):
        """saves credential objects to credentials_list"""
        self.credentials_list.append(self)

    def delete_credential(self):
        """deleting a particular credential"""
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_name(cls, account_name):
        """receiving  in a name and returning a credential that matches that particular name
        Arguments: name: acct_name that has a password
        Returns: The acct_name and it's corresponding PassWord
        """

        for credential in cls.credentials_list:
            if credential.account_name == account_name:
                return credential

    @classmethod
    def credential_exists(cls, name):
        """ check if a credential exists
        Arguments:
        name: name of acct to search if it exists
        boolean: True or False depending if the contatc exists
        """

        for credential in cls.credentials_list:
            if credential.account_name == name:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        """displays all recent credentials"""
        return cls.credentials_list

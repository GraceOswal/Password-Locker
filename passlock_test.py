import unittest
from passlock import User
import pyperclip
from launchpadlib.credentials import Credentials



class TestClass(unittest.TestCase):
    """
    This Test class defines test cases for the User class.
    """
    def setUp(self):
        """
        This method runs before each individual test methods runself.
        """

        self.new_user = User ("Swift","Gracegee","grcee")

    def test_unit(self):
        """
        test_init test case to test if the object is initialized properly
        """

        self.assertEqual(self.new_user.username,"Gracegee")
        self.assertEqual(self.new_user.password, "grcee")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the
        user list
        '''
        self.new_user.save_user() #this saves new user
        self.assertEqual(len(User.user_list),1)

    class CredentialsTestClass(unittest.TestCase):
        """
        Test class that defines test cases for credentials class
        """
        def setUp(self):
            """
            This method runs before each individual credentials test methods' runs
            """

            self.new_credentials = Credentials("Swift","Gracegee","grcee")

        def test_init(self):
            """
            Test case that checks if new Credentials instance has been initialized properly
            """
            self.assertEqual(self.new_credentials.account,"Swift")
            self.assertEqual(self.new_credentials.username,"Gracegee")
            self.assertEqual(self.new_credentials.password,"grcee")

    def test_save_credential(self):
        """
        test case to test if the credential object is saved into the credentials list.
        """
        self.new_credentials.save_details()
        self.assertEqual(len(Credentials.credentials_list),1)

    def tearDown(self):
        '''
        method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []

#other test cases here

    def test_save_multiple_accounts(self):
        '''
        test_save_multiple_account to check if we can save
        many account details
        '''
        self.save_credentials()
        test_Credentials = Credentials("Gmail","kinyuagee","ntongu") #new credentials
        test_Credentials.Credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credentials(self):
        """
        test_delete_credentials to test if we can remove an account from our
        credential list
        """
        self.Credentials.save_credentials()
        test_credentials = Credentials("Gmail","kinyuagee","ntongu")
        test_credentials.save_details()

        self.credentials.delete_credentials()  #deleting saved details
        self.assertEqual(len(Credentials.credential_list),2)

    def test_find_credentials_by_account(self):
        """
        test_find_credentials checks if we can find a credential entry by its
        account name and display the details of the credential
        """
        self.Credentials.save_details()
        test_credentials = Credentials("Gmail","kinyuagee","ntongu")
        test_credentials.save_details()

        found_credential = Credentials.find_by_account("Gmail")
        self.assertEqual(found_credential.account,test_credentials.account)

    def test_credential_exists(self):
        """
        test to check if we can return a true or false based on whether we find or can't find the credential.
        """
        self.credentials.save_details()
        test_credentials = Credentials("Gmail", "kinyuagee", "ntongu")
        test_credentials.save_details()

        credential_exists = Credentials.credential_exist("Gmail")
        self.assertTrue(credential_exists)

    def test_display_credentials(self):
        '''
        method that displays all the credentials
        that has been saved by the user
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

    def test_copy_password(self):
        '''
        Test to confirm that we are copying the password from found account
        '''

        Credentials.copy_password("ntongu")

        self.assertEqual(self.new_credentials.password,pyperclip.paste())




if __name__ == '__main__':
    unittest.main()
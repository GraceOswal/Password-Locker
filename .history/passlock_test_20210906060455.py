import unittest
from passlock import User
from passlock import Credentials
import pyperclip

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
        self.assertEqual(self.new_user.password, "grce")
        
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the
        user list
        '''
        self.new_user.save_user() #this saves new user
        self.assertEqual(len(User.user_list),1)
        
    class TestCredentials(unittest.TestCase):
        """
        Test class that defines test cases for credentials class
        """
        def setUp(self):
            """
            This method runs before each individual credentials test methods' runs
            """
            
            self.new_credential = Credentials("Swift","Gracegee","grcee")
            
        def test_init(self):
            """
            Test case that checks if new Credentials instance has been initialized properly
            """
            self.assertEqual(self.new_credential.account,"Swift")
            self.assertEqual(self.new_credential.username,"Gracegee")
            self.assertEqual(self.new_credential.password,"grcee")
            
    def save_credential_test(self):
        """
        test case to test if the crential object is saved into the credentials list.
        """
        self.new_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),1)

    def tearDown(self):
        '''
        method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []
        
    def test_save_multiple_accounts(self):
        '''
        test_save_multiple_account to check if we can save
        many account details
        '''
        self.new_credential.save_details()
        test_credential = Credentials("Gmail","kinyuagee","ntongu") #new credentials
        test_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),2)
        
    def test_delete_credentials(self):
        """
        test_delete_credentials to test if we can remove an account from our
        credential list
        """
        self.new_credentials.save_details()
        test_credentials = Credentials("Gmail","kinyuagee","ntongu")
        test_credentials.save_details()
        
        self.new_credentials.delete_credentials()  #deleting saved details
        self.assertEqual(len(Credentials.credential_list),2)
        
    def test_find_credentials(self):
        """
        test_find_credentials checks if we can find a credential entry by its 
        account name and display the details of the credential
        """
        self.new_credential.save_details()
        test_credential = Credentials("Gmail","kinyuagee","ntongu")
        test_credential.save_details()
        
        found_credential = Credentials.find_by_account("Gmail")
        self.assertEqual(found_credential.account,test_credential.account)
        
    def test_credential_exist(self):
        """
        test to check if we can return a true or false based on whether we find or can't find the credential.
        """
        self.new_credential.save_details()
        test_credential = Credentials("Gmail", "kinyuagee", "ntongu")  
        test_credential.save_details()

        credential_exists = Credentials.credential_exist("Gmail")
        self.assertTrue(credential_exists)

    def test_display_all_saved_credentials(self):
        '''
        method that displays all the credentials 
        that has been saved by the user
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)
        
    def test_copy_password(self):
        '''
        Test to confirm that we are copying the password from found account
        '''
        
        self.new_credentials.save_details()
        Credentials.copy_password("ntongu")
        
        self.assertEqual(self.new_credentials.password,pyperclip.paste())
        
    

        
if __name__ == '__main__':
    unittest.main()
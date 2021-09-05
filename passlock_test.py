import unittest
from passlock import User
from passlock import Credentials

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

        
if __name__ == '__main__':
    unittest.main()
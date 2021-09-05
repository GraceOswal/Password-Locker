import unittest #Importing the unittest module
from passlock import User  #this imports the user class
from passlock import Credentials  #this imports the credential class

class TestClass(unittest.TestCase):
    """
    This test defines the test cases for the behaviour of user classself.
    """
    
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Gracegee","grcee") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"Gracegee")
        self.assertEqual(self.new_user.password,"grcee")


if __name__ == '__main__':
    unittest.main()
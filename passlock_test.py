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
        
if __name__ == '__main__':
    unittest.main()
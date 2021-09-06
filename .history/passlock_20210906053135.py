import random
import string
import pyperclip
class User:
    """
    Class that generates new instances of contacts.
    """

    user_list = []   #Empty user list
    
    def __init__(self,username,password):
        
        #docstring removed for simplicity
    
            self.username = username
            self.password = password
            
    def save_user (self):
        """
        A method that saves a new user instance into the user list
        """
        User.user_list.append(self)
        
            
    @classmethod
    def display_user(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list
    
    def delete_user (self):
        '''
        delete_account method removes a saved existing account
        '''
        User.user_list.remove(self)
    
    class Credentials():
        """
        This class creates credentials that help create new objects of credentials
        """
        
    credentials_list = []
        
    @classmethod
    def verify_user(cls,username, password):
        """
        method to verify whether the user is in our user_list or not
        """
        a_user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                    a_user == user.username
        return a_user

    def __init__(self,account,userName, password):
        """
        method that defines user credentials to be stored
        """
        self.account = account
        self.userName = userName
        self.password = password
    
    def save_details(self):
        """
        method to store a new credential to the credentials list
        """
        Credentials:any.credentials_list.append(self)

    def delete_credentials(self):
        """
        delete_credentials method that deletes an account credentials from the credentials_list
        """
        Credentials:any.credentials_list.remove(self)
    
    @classmethod
    def find_by_account(cls, account):
        """
        Method that takes in a account_name and returns a credential that matches that account_name.
        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential
   
    @classmethod
    
    def if_credential_exist(cls, account):
        """
        Method that checks if a credential exists from the credential list
        and returns true or false depending if the credential exists.
        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return True
        return False
    
    @classmethod
    
    def display_credentials(cls):
        """
        Method that returns all items in the credentials list
        """
        return cls.credentials_list
    
    @classmethod
    
    def copy_password(cls, account):
        found_account = Credentials.find_by_account(account)
        pyperclip.copy(found_account.password)

    def generatePassword(self.stringLength=8):
        """
        Generate a random password string of letters and digits and special characters"""
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
        return ''.join(random.choice(password) for i in range(stringLength))
    
import unittest # importing the unittest module
from user import User
from credential import credentials
import pyperclip
"""
unittest.TestCase: TestCase class that helps in creating test cases
"""
class TestUser(unittest.TestCase):
    """
    test class that defines test cases for the user class behaviours
    """
    def setUp(self):
        """
        set up method to run before each test case
        """
        self.new_user = User("facebook","manka","2999") # crreate user objects
    def tearDown(self):
        '''
        method that does clean up after each test case has run.
        '''
        User.user_list=[]
    def test__init__(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.name,"facebook")
        self.assertEqual(self.new_user.username,"manka")
        self.assertEqual(self.new_user.password,"2999")
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list), 1)
    def test_save_multipe_users(self):
        '''
        test_save_multiple_users to check if we can save multiple user objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("twitter", "max", "5443") # new user
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = User("instagram","loop","334") # new user
        test_user.save_user()
        self.new_user.delete_user() # delete user object
        self.assertEqual(len(User.user_list),1)
    def test_find_user_by_username(self):
        '''
        test to check if we can find a user by username and display information
        '''
        self.new_user.save_user()
        test_user = User("ig", "humo", "334") # new user
        test_user.save_user()
        found_user = User.find_by_username("humo")
        self.assertEqual(found_user.password,test_user.password)
    def test_user_exists(self):
        '''
        test to check if we can return a boolean if we cannot find the user
        '''
        self.new_user.save_user()
        test_user = User("twitter", "ty", "667") # new user
        test_user.save_user()
        user_exists = User.user_exists("ty")
        self.assertTrue(user_exists)
    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''
        self.assertEqual(User.display_users(),User.user_list)
    def set_Up(self):
        '''
        set up method that runs before each Test
        '''
        self.new_credentials = credentials("twitter","billowbashir","123456789")
    def tear_Down(self):
        '''
        method that does clean up after each test case has run.
        '''
        credentials.credentials_list=[]
    def test_init(self):
        self.assertEqual(self.new_credentials.platform_name,"twitter")
        self.assertEqual(self.new_credentials.user_name,"billowbashir")
        self.assertEqual(self.new_credentials.password,"123456789")
    def test_save_credentials(self):
        '''
        test case to test if the object is saved into the credentials_list
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(credentials.credentials_list),1)
    def test_save_multiple_credentials(self):
        '''
        test case to test if we can save multiple credentials into the credentials_list
        '''
        self.new_credentials.save_credentials()
        test_credentials = credentials("test","testname","987654321")
        test_credentials.save_credentials()

        self.assertEqual(len(credentials.credentials_list),2)
    def test_delete_credentials(self):
        '''
        test case to test if we can delete credentials from the credentials_list
        '''
        self.new_credentials.save_credentials()
        test_credentials = credentials("test","testname","987654321")
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials()
        self.assertEqual(len(credentials.credentials_list),1)
    def test_find_credentials_by_platform_name(self):
        '''
        test case to test if we can search for credentials in the credentials_list by the platform_name and display
        '''
        test_credentials = credentials("test","testname","987654321")
        test_credentials.save_credentials()

        found_credential=credentials.find_credentials_by_platform_name("test")
        self.assertEqual(found_credential.username,test_credentials.user_name)
    def test_credentials_exists(self):
        '''
        test case to test whether we can return a boolean value if we cannot find the credentials we search for
        '''
        test_credentials = credentials("test","testname","987654321")
        test_credentials.save_credentials()
        credentials_exists= credentials.credential_exists("test")

        self.assertTrue(credentials_exists)
    def test_display_all_credentials(self):
        '''
        test case to test whether we can display a list of all save credentials
        '''
        self.assertEqual(credentials.display_all_credentials(),credentials.credentials_list)




if __name__ == '__main__':
    unittest.main()
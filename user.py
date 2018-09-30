import unittest
class User:
    """
    Class that generates new instances of contacts.
    """

    user_list = [] # empty user list

    def __init__(self,name,username,password):
        self.name = name
        self.username = username
        self.password = password

        """
        __init__ method that helps us define properties for our objects.
        """    
    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''
        User.user_list.append(self)
    def delete_user(self):
        '''
        delete_user_method deletes a saved user from the user_list
        '''
        User.user_list.remove(self)
    @classmethod
    def find_by_username(cls,username):
        '''
        method that takes in a username and returns a user that matches that username
        '''
        for user in cls.user_list:
            if user.username == username:
                return user
    @classmethod
    def user_exists(cls,username):
        '''
        method that checks if a user exists froom the user list
        '''
        for user in cls.user_list:
            if user.username == username:
                return True
        return False
    @classmethod
    def display_users(cls):
        '''
        method that returns a list of all users saved
        '''
        return cls.user_list



if __name__ == '__main__':
    unittest.main()
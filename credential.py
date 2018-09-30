import pyperclip
class credentials:
    '''
    class to save the user class information
    '''
    credentials_list = []

    def __init__(self,name,username,password):
        self.platform_name = name
        self.user_name = username
        self.password = password
    def save_credentials(self):
        '''
        method to save credential to credential list
        '''
        credentials.credentials_list.append(self)
    def delete_credentials(self):
        '''
        method to delete credentials from credentials list
        '''
        credentials.credentials_list.remove(self)
    @classmethod
    def find_credentials_by_platform_name(cls,username):
        '''
        method to find credentials from credential list
        '''
        for credential in cls.credentials_list:
            if credential.username == username:
                return credential
    @classmethod
    def credential_exists(cls,username):
        '''
        method to search through the credentials_list by platform_name and return the credentials
        '''
        for credential in cls.credentials_list:
            if credential.username == username:
                return True
        return False
    @classmethod
    def display_all_credentials(cls):
        '''
        method to display list of saved credentials
        '''
        return cls.credentials_list








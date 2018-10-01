#!/usr/bin/env python3.6
#!/bin/python3.6
from user import User
import random
import pyperclip
def create_user(p_name,u_name,ps):
    '''
    function to create a new user
    '''
    new_user = User(p_name,u_name,ps)
    return new_user
def save_user(user):
    '''
    function to save user
    '''
    user.save_user()
def del_user(user):
    '''
    function to delete a user
    '''
    user.del_user()
def find_user(username):
    '''
    function that finds a user by platform_name and returns the user
    '''
    return User.find_by_username(username)
def check_existing_user(username):
    '''
    function that check if a user exists with that platform_name and return a boolean
    '''
    return User.user_exists(username)
def display_user():
    '''
    function that returns all the saved users
    '''
    return User.display_users()
def copy_password(username):
     '''
     function to copy password to the clipboard
    '''
     my_password = UserData.show_user_data(username)
     pyperclip.copy(my_password.password)

def main():
    print('Hello! welcome to your password locker. what is your name?')
    platform_name = input()
    print(f'hello {platform_name} what do you want to acess?')
    print('\n')
    while True:
        print('Use these short codes: sp - save password, gp - generate password, cp - copy password, dp - display passwords, fp - find passwords, ex - exit ')
        short_code = input().lower()
        if short_code == 'sp':
            print ('new user')
            print('-'*10)
            print('platform_name')
            p_name = input()
            print('username')
            u_name = input()
            print('password')
            ps = input()
            save_user(create_user(p_name,u_name,ps)) # create and save new user
            print('\n')
            print(f'new user {p_name} created')
            print('\n')
        elif short_code == 'gp':
            print("New password")
            print("-"*10)

            print ("platform name ....")
            pname = input()

            print("username ...")
            uname = input()
            chars = 'abcdefghijklmnopqrstuvwxyz123456789'
            password = ''
            print('dictate the length of your password')
            r  = int(input())
            for c in range(r):
                password= random.choice(chars)
                print(password, end="")
            save_user(create_user(pname,uname,password)) # create and save new credentials.
            print ('\n')
            print(f"New password for {pname} and account {uname} created")
            print ('\n')
        elif short_code == 'dp':
            if display_user():
                print('here are your users')
                print('make a password for viewing your credentials')
                ps = input()
                print('password...')
                password = input()
                if password == ps:
                    for user in display_user():
                        print(f'{user.name} {user.username}..{user.password}')
                        print('\n')
                else:
                    print('you entered wrong password')
            else:
                print('/n')
                print('you dont seem to have the user saved yet')
                print('\n')
        elif short_code == 'fp':
            print('enter the platform you want to search for')
            search_platform_name = input()
            if check_existing_user(search_platform_name):
                search_platform_name = find_user(search_platform_name)
                print(f'{search_platform_name.username}{search_platform_name.name}')
                print('-'*20)
                print(f'password is {search_platform_name.password}')
            else:
                print('the user does not exist')
        elif short_code =="cp":
            print("Enter the user name of  password you want to copy")
            user_found = input()
            if check_existing_user(user_found):
                user_found = User.find_by_username(user_found)
                pyperclip.copy(user_found.password)
                print("\n")
                print(f"Password is successfully copied to clipboard, go ahead and paste it")
            else:
                print("You do not have any passwords yet")
                print("--"*10)
        elif short_code == "ex":
            exit()
        else:
            print('you did not use the short_code!!!')




    

if __name__ == '__main__':
    main()



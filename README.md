# Password-locker
***
# Description
PasswordLocker is a python application that generates and saves passwords for various user accounts.
***
# Setup and Installation
* git clone the repo
* download python3.6
* run this commands:
* chmod +x run.py
* ./run.py
***
# Known Bugs
* the pyperclip is copying one character of the password
***
# Technologies Used
* python3.6 shell
***
# Specifications
| Behavior        | Input           | Outcome  |
| ------------- |:-------------:| -----:|
| user chooses wrong shortcode |choose wrong short code | error message 'you have choosen wrong short code |
| If user chooses shortcode for saving password| choose 'sp' | a password will be saved|
| If user chooses shrtcode for generating password | choose 'gp'| a new password will be generated for him |
| If user chooses shortcode for displaying password |  choose 'dp'| all saved password will be displayed |
| If user chooses shortcode for find password | choose 'fp'| the username and password wil be duispalyed |
|if user wants to copy password to clipboard| choose 'cp'|the password will be copied to clipboard|
|If user wants to exit| choose 'ex'| the program will be exited from|

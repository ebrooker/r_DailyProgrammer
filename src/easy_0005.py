'''
Ezra S. Brooker
Date Created: 2021-07-03

Your challenge for today is to create a program which is password protected, 
and wont open unless the correct user and password is given.

For extra credit, have the user and password in a seperate .txt file.

For even more extra credit, break into your own program :)

'''

import sys
if sys.version[0] != '3':
    raise Exception("Python 2 is no longer supported, please use Python 3")


def login_node():
    
    with open("../logs/easy_0005_login.txt", "r") as fin:
        user = fin.readline().strip()
        pswd = fin.readline().strip()

    attempts = 5
    while True:

        user_attempt = input("username: ")
        pswd_attempt = input("password: ")
        attempts-=1

        if user_attempt == user and pswd_attempt == pswd:
            break

        elif attempts == 0:
            sys.exit("[Login Failed] Too many login attempts made, aborting program...")

        else:
            print(f"[Login Error] Incorrect username and/or password, {attempts} login attempts remaining")


if __name__ == '__main__':

    login_node()
    print("\nYou have successfully logged into your own program!\n")

'''
Ezra S. Brooker
Date Created: 2021-07-02

https://www.reddit.com/r/dailyprogrammer/comments/pm6oj/2122012_challenge_4_easy/

You're challenge for today is to create a random password generator!

For extra credit, allow the user to specify the amount of passwords to generate.

For even more extra credit, allow the user to specify the length of the strings
they want to generate!

'''

import sys
if sys.version[0] != '3':
    raise Exception("Python 2 is no longer supported, please use Python 3")
from random import sample
from datetime import datetime

class PasswordGenerator:

    __ASCIIBET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=<>?,/;[]}{1234567890'
    __LENASCII = len(__ASCIIBET)
    

    def __init__(self,npass=1,pwlen=16):

        self.__npass = npass
        self.__pwlen = pwlen


    def clear(self):
        self.__PASSWORDS = []


    def set_asciibet(self,asciibet):
        self.__ASCIIBET = asciibet        


    def print_passwd(self):
        [print(pw) for pw in self.__PASSWORDS]


    def gen_passwd(self,npass=None, pwlen=None):

        if npass is not None:
            self.__npass = npass 
        
        if pwlen is not None:
            self.__pwlen = pwlen

        self.__PASSWORDS = {''.join(s for s in sample(self.__ASCIIBET,self.__pwlen)) : datetime.now() for _ in range(self.__npass)}


    def save_passwd(self,file=None):

        if file is not None:
            self.__file = file
        else:
            self.__file = "../logs/easy_0004_passwd.log"

        with open(self.__file, "a") as fout:
            [fout.write(f"{v} : {k}\n") for k,v in self.__PASSWORDS.items()]


if __name__ == '__main__':

    # Generates, prints, and saves to file the number of and length of passwords specified
    pw = PasswordGenerator()
    pw.gen_passwd(
            npass = int(input("Number of passwords to generate: ")),
            pwlen = int(input("Length of passwords to generate: "))
            ) 
    pw.print_passwd()
    pw.save_passwd()
    pw.clear()
    pw.print_passwd()

    pw.set_asciibet("qwertyuioplkjhgfdsamnbvcxz0987654321")
    pw.gen_passwd(
            npass = int(input("Number of passwords to generate: ")),
            pwlen = int(input("Length of passwords to generate: "))
            ) 
    pw.print_passwd()
    pw.save_passwd()
    pw.clear()
    pw.print_passwd()

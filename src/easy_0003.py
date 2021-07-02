'''
Ezra S. Brooker
Date Created: 2021-07-01

Welcome to cipher day!

Write a program that can encrypt texts with an alphabetical caesar cipher. 
This cipher can ignore numbers, symbols, and whitespace.

For extra credit, add a "decrypt" function to your program!

'''

import sys
if sys.version[0] != '3':
    raise Exception("Python 2 is no longer supported, please use Python 3")
import copy
from random import randint

from IPython import embed

class CaeserCipher:
    ''' Expanded this Caeser Cipher to lower/uppercase, symbols, and numbers you
    just have to make sure that you record the length of whatever ASCII-bet you
    use to ensure the cipher works as intended.
    '''

    __LOWERBET = 'abcdefghijklmnopqrstuvwxyz'
    __UPPERBET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    __SYMBOBET = '!@#$%^&*()_+-=<>?:,./;[]{}|`~'
    __NUMBABET = '1234567890'
    __ASCIIBET = f"{__LOWERBET}{__UPPERBET}{__NUMBABET}{__SYMBOBET}"
    __LENASCII = len(__ASCIIBET)

    def __init__(self, shift=0):

        self.set_shift(shift)

    def set_shift(self,shift=0):
        while shift <= 0:
            shift = randint(1,10000)%randint(1,self.__LENASCII-1)
        self.__shift = shift

    def get_shift(self):
        return self.__shift

    def set_asciibet(self,asciibet):
        self.__ASCIIBET = asciibet
        self.__LENASCII = len(self.__ASCIIBET)

    def get_asciibet(self):
        return self.__ASCIIBET

    def encrypt(self,text):
        self.__encryption = self.__cipher(text, encrypt=True)
        return self.__encryption

    def decrypt(self):
        self.__decryption = self.__cipher(self.__encryption, encrypt=False)
        return self.__decryption

    def __cipher(self,text,encrypt):
        newtext = ''
        for i,s in enumerate(text):
            if s == ' ':
                newtext+=s
                continue
            if encrypt:
                newtext += self.__ASCIIBET[(self.__ASCIIBET.index(s) + \
                                            self.get_shift()) % self.__LENASCII]
            else:
                newtext += self.__ASCIIBET[(self.__ASCIIBET.index(s) - \
                                            self.get_shift()) % self.__LENASCII]
        return newtext

if __name__ == '__main__':

    cipher = CaeserCipher()
    encrypted = cipher.encrypt("Hello World!")
    decrypted = cipher.decrypt()
    print(f"Encrypted Text: {encrypted}")
    print(f"Decrypted Text: {decrypted}")
        
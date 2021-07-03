'''
Ezra S. Brooker
Date Created: 2021-07-01

https://www.reddit.com/r/dailyprogrammer/comments/pkwb1/2112012_challenge_3_intermediate/

Welcome to cipher day!

Create a program that can take a piece of text and encrypt it with an alphabetical
substitution cipher. This can ignore white space, numbers, and symbols.

For extra credit, make it encrypt whitespace, numbers, and symbols!

For extra extra credit, decode someone elses cipher!

'''

import sys
if sys.version[0] != '3':
    raise Exception("Python 2 is no longer supported, please use Python 3")
import copy
from random import sample, randint

from IPython import embed


class VigenereCipher:
    ''' This uses the Vigenere Cipher '''

    __LOWERBET = 'abcdefghijklmnopqrstuvwxyz'
    __UPPERBET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    __SYMBOBET = '!@#$%^&*()_+-=<>?:,./;[]{}|`~\'\"'
    __NUMBABET = '1234567890'
    __ASCIIBET = f"{__LOWERBET}{__UPPERBET}{__NUMBABET}{__SYMBOBET}"
    __LENASCII = len(__ASCIIBET)

    def __init__(self, key=None):
        self.set_key(key)


    def set_key(self,key=None):
        if key is None:
            # Generate random key
            self.__key = sample(self.__ASCIIBET, randint(1,len(self.__ASCIIBET)//10))
        else:
            self.__key   = key

        self.__set_shift()

    def get_key(self):
        return self.__key

    def __set_shift(self):
        self.__shift = len(self.__key)

    def get_shift(self,i):
        return i % self.__shift

    def set_asciibet(self,asciibet):
        self.__ASCIIBET = asciibet
        self.__LENASCII = len(self.__ASCIIBET)

    def get_asciibet(self):
        return self.__ASCIIBET

    def encrypt(self,text):
        self.__original = text
        self.__encryption = self.__cipher(text, encrypt=True)
        return self.__encryption

    def decrypt(self):
        self.__decryption = self.__cipher(self.__encryption, encrypt=False)
        return self.__decryption

    def get_encoding(self):
        self.__encoding   = self.__encode(self.__original)
        return self.__encoding

    def print_info(self):
        self.get_encoding()
        print(f"\nOriginal  Text: \n{self.__original}  ")
        print(f"\nEncrypted Text: \n{self.__encryption}")
        print(f"\nEncoding  Text: \n{self.__encoding}  ")
        print(f"\nDecrypted Text: \n{self.__decryption}")
        print(f"\nEncryption Key: {self.__key}       \n")


    def __encode(self,text):
        newtext = ''
        i = 0
        for s in text:
            if s == ' ':
                newtext+=s
            else:
                newtext += self.__key[self.get_shift(i)]
                i+=1
        return newtext

    def __cipher(self,text,encrypt):
        newtext = ''
        i=0
        for s in text:
            if s not in self.__ASCIIBET:
                newtext+=s
                continue
            if encrypt:
                newtext += self.__ASCIIBET[(self.__ASCIIBET.index(s) + \
                                            self.get_shift(i)) % self.__LENASCII]
            else:
                newtext += self.__ASCIIBET[(self.__ASCIIBET.index(s) - \
                                            self.get_shift(i)) % self.__LENASCII]
            i+=1

        return newtext

if __name__ == '__main__':


    text = "That though the radiance which was once so bright be now forever taken from my sight. \n\
    Though nothing can bring back the hour of splendor in the grass, glory in the flower. We will \n\
    grieve not, rather find strength in what remains behind."


    cipher = VigenereCipher(key="calorie")
    cipher.encrypt(text)
    cipher.decrypt()
    cipher.print_info()



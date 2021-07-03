'''
Ezra S. Brooker
Date Created: 2021-07-01

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


    text = "Look, having nuclear - my uncle was a great professor and scientist and engineer, \n\
Dr. John Trump at MIT; good genes, very good genes, OK, very smart, the Wharton \n\
School of Finance, very good, very smart - you know, if you\'re a conservative \n\
Republican, if I were a liberal, if, like, OK, if I ran as a liberal Democrat, they \n\
would say I\'m one of the smartest people anywhere in the world - it\'s true! - but \n\
when you\'re a conservative Republican they try - oh, do they do a number - that\'s why\n\
I always start off: Went to Wharton, was a good student, went there, went there, did\n\
this, built a fortune - you know I have to give my like credentials all the time, \n\
because we\'re a little disadvantaged - but you look at the nuclear deal, the thing \n\
that really bothers me - it would have been so easy, and it\'s not as important as \n\
these lives are - nuclear is so powerful; my uncle explained that to me many, many \n\
years ago, the power and that was 35 years ago; he would explain the power of what\'s \n\
going to happen and he was right, who would have thought? - but when you look at \n\
what\'s going on with the four prisoners - now it used to be three, now it\'s four - but\n\
when it was three and even now, I would have said it\'s all in the messenger; fellas, \n\
and it is fellas because, you know, they don\'t, they haven\'t figured that the women are\n\
smarter right now than the men, so, you know, it\'s gonna take them about another 150 \n\
years - but the Persians are great negotiators, the Iranians are great negotiators, so, \n\
and they, they just killed, they just killed us, this is horrible."


    cipher = VigenereCipher(key="covfefe")
    cipher.encrypt(text)
    cipher.decrypt()
    cipher.print_info()



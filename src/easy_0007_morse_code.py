'''
Ezra S. Brooker
Date Created: 2021-07-03

https://www.reddit.com/r/dailyprogrammer/comments/pr2xr/2152012_challenge_7_easy/

Write a program that can translate Morse code in the format of ...---...

A space and a slash will be placed between words. ..- / --.-

For bonus, add the capability of going from a string to Morse code.

Super-bonus if your program can flash or beep the Morse.

This is your Morse to translate:

.... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. 
/ --. --- --- -.. / .-.. ..- -.-. -.- / --- -. / - .... . 
/ -.-. .... .- .-.. .-.. . -. --. . ... / - --- -.. .- -.--

Personal Bonus: Add capability of using different version of morse code.

Personal Bonus: Enable support for numeric text and some symbolic text.

Personal Bonus: Add capability to pass in custom Morse Code standard, which needs
                to have corresponding ASCIIBET passed in with it to prevent errors.

'''

import sys
if sys.version[0] != '3':
    raise Exception("Python 2 is no longer supported, please use Python 3")
import re

from IPython import embed

class MorseCode:

    __ASCIIBET    = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,?!\'\"()&:;/_=+-$@"

    __INTERNATIONAL_MORSE  = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. \
                     -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.. \
                     ----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----. \
                     .-.-.- --..-- ..--.. -.-.-- .----. .-..-. -.--. -.--.- .-... \
                     ---... -.-.-. -..-. -...- .-.-. -....- ...-..- .--.-.".split()
                     # ORDERED BY LINE: A-L  M-Z  0-9  .,?!\'\"()&  :;/_=+-$@


    __MORSE_VERS  = [ "international" ]
    __MORSE_LIST  = [ __INTERNATIONAL_MORSE ]
    __MORSE_DICT  = dict( zip( __MORSE_VERS, __MORSE_LIST ) )

    def __init__(self, morse_string=None, text_string=None, morse_code="international"):

            self.set_morse_string(morse_string)
            self.set_text_string(text_string)
            self.set_morse_code_version(morse_code)

    def set_morse_string(self, morse_string=None):
        self.__morse = morse_string

    def get_morse_string(self):
        return self.__morse

    def set_text_string(self, text_string=None):
        if text_string is not None:
            text_string = text_string.upper()
        self.__text = text_string

    def get_text_string(self):
        return self.__text

    def set_morse_code_version(self, morse_code="international"):
        print(f"\n[Translator] Using {morse_code.upper()} morse code\n")
        try:
            self.__morse_code = morse_code
            self.__MORSEBET   = self.__MORSE_DICT[morse_code.lower()]
        except:
            print(f"\n[Translate Error] Unrecognized version of Morse Code requested...")
            print(f"                  Please choose from the following list:")
            print(f"                  {self.__MORSE_VERS}\n")

    def get_morse_code_version(self):
        # Return version name of Morse Code and the Morse "ASCIIBET"
        return self.__morse_code, self.__MORSEBET

    def add_morse_code_version(self,name,morsebet):
        self.__MORSE_VERS.append(name)
        if type(morsebet) is list: self.__MORSE_LIST.append(morsebet)

    def morse_code_versions(self):
        print(f"Available Morse Code versions: {self.__MORSE_VERS}")


    def translate(self, text_string=None, morse_string=None, mode='morse'):

        if text_string is not None:
            self.set_text_string(text_string)

        if morse_string is not None:
            self.set_morse_string(morse_string)

        if mode.lower() == 'morse':
            self.__morse2text()

        elif mode.lower() == 'text':
            self.__text2morse()

        else:
            sys.exit("\n[Translate Error] Unrecognized translation mode, please select \"morse\" or \"text\"")

    def __morse2text(self):
        if self.__morse is not None:
            self.__text = ''.join(f"{''.join(self.__ASCIIBET[self.__MORSEBET.index(letter)] for letter in word.split())} " 
                                                                                    for word in self.__morse.split(' / '))
        else:
            print("\n[Translate Error] No morse code to translate into text\n")

    def __text2morse(self):
        if self.__text is not None:
            self.__morse = ''.join(f"{' '.join(' '.join({self.__MORSEBET[self.__ASCIIBET.index(letter)]}) for letter in word)} / " 
                                                                                    for word in self.__text.split())

        else:
            print("\n[Translate Error] No text to translate into morse code\n")
                

if __name__ == '__main__':

    # Test 1
    morse = ".... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. / --. --- --- -.. / .-.. ..- -.-. -.- / --- -. / - .... . / -.-. .... .- .-.. .-.. . -. --. . ... / - --- -.. .- -.--"
    translator = MorseCode(morse_string=morse)
    translator.translate(mode='morse')
    print(morse)
    print(translator.get_text_string())
    print("")

    # Test 2
    text  = "My god Its full of 109 stars!?"
    translator.translate(text_string=text, mode='text')
    new_morse = translator.get_morse_string()
    translator.translate(morse_string=new_morse, mode='morse')
    new_text = translator.get_text_string()
    print(text)
    print(new_morse)
    print(new_text)
    print("")
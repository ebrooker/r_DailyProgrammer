'''
Ezra S. Brooker
Date Created: 2021-07-02

https://www.reddit.com/r/dailyprogrammer/comments/pm6sq/2122012_challenge_4_intermediate/

Create a calculator program that will take an input, following normal 
calculator input (5*5+4) and give an answer (29). This calculator 
should use all four operators.

For extra credit, add other operators (6(4+3), 3 ** 3, etc.)

'''

import sys
if sys.version[0] != '3':
    raise Exception("Python 2 is no longer supported, please use Python 3")


if __name__ == '__main__':

    while True:
        read = input("Enter calculation or <q> to quit: ")
        if "q" in read.lower():
            break
        try:
            print(eval(read))
        except:
            print("[ReadError] Invalid input")

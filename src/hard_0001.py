'''
Ezra S. Brooker
2021

Source: reddit.com/r/DailyProgrammer 2012-02-10
https://www.reddit.com/r/dailyprogrammer/comments/pihtx/intermediate_challenge_1/


We all know the classic "guessing game" with higher or lower prompts. Lets do a role 
reversal; you create a program that will guess numbers between 1-100, and respond 
appropriately based on whether users say that the number is too high or too low. 
Try to make a program that can guess your number based on user input and great code!

'''
import sys
if sys.version[0] != '3':
    raise Exception("Python 2 is no longer supported, please use Python 3")
from random import randint

class RandomGuesser:
    low   = 1
    high  = 100
    guess = 0

    def __init__(self):

        self.start_game()

    def start_game(self):

        number = int(input("Please enter a number between 1-100, I promise I won't look at it: "))
        while True:
            if type(number) is int:
                break
            else:
                number = input("Non-integer detected! Enter an integer number betwen 1-100: ")
            
        self.number = number

        while True:

            self.guess = randint(self.low,self.high)

            print(f"\nIs {self.guess} your number?")
            print(f"    1. Yes!"         )
            print(f"    2. No! Lower..." )
            print(f"    3. No! Higher...")

            ans = 0
            while ans not in [1,2,3]:
                ans = int(input("\nEnter 1, 2, or 3: "))

            if ans==1:
                print("\nYay! Thanks for playing!\n")
                break
            elif (ans==2 or ans==3) and self.guess == self.number:
                print("\nYou said your number was {self.number}, you're lying! I win!\n")
                break
            elif ans==2:
                self.high = self.guess-1
            elif ans==3:
                self.low = self.guess+1

        self.low = 1
        self.high = 100
        self.guess = 0

if __name__ == '__main__':

    Guesser = RandomGuesser()

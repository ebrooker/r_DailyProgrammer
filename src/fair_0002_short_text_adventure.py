'''
Ezra S. Brooker
Date Created: 2021-07-01

https://www.reddit.com/r/dailyprogrammer/comments/pjbuj/intermediate_challenge_2/

Create a short text adventure that will call the user by their name. 
The text adventure should use standard text adventure commands ("l, n, s, e, i, etc.").

For extra credit, make sure the program doesn't fault, quit, glitch, fail, or loop no matter 
what is put in, even empty text or spaces. These will be tested rigorously!

For super extra credit, code it in C

'''

import sys
if sys.version[0] != '3':
    raise Exception("Python 2 is no longer supported, please use Python 3")

import time
import random
from string import ascii_letters

class TextAdventure:

    __RANDEAD = random.randint(1,10)

    __DEATHEVENT = [
        "bandits murdered you in your sleep...", "you were attacked by a hungry bear...",
        "a tree fell on top of you...", "it seems some berries you ate didn't agree with you...",
        "you passed away peacefully in your sleep...", "something... from the sky abducted you..."
        ]

    __COMPASS = ['(n)orth', '(e)ast', '(s)outh', '(w)est']

    __HORIZON = [
        "a mountain range.", "a green meadow.",   "a clean lake.",   "a dark forest.", 
        "a large castle.",   "a quaint village.", "a lonely cottage.", "a winding trail."
    ]

    __LAST_DIRECTION = ''

    def __init__(self):

        self.day  = 0
        self.name = input("\nGreetings adventurer! Doth thou have a name? ")

        if random.choice(ascii_letters) in self.name:
            print(f"Ah, {self.name} thine name is a good one. Ye may find this journey well rewarding.\n")
        else:
            print(f"Heaven above, ye name is {self.name}?! Ye may find this journey filled with misfortune.\n")

        print(f"Ye are forewarned {self.name}, once ye begin this journey, ye can never turn back.\n")


    def __print_directions(self):

        print(f"\n[Day {self.day}] Ye take a look at your surroundings")
        print(f"{self.name}, which way shall ye go?")
        ind = random.sample(range(len(self.__HORIZON)), 4)
        if self.__LAST_DIRECTION != 'n': print(f"Go (n)orth towards {self.__HORIZON[ind[0]]}")
        if self.__LAST_DIRECTION != 'e': print(f"Go (e)ast  towards {self.__HORIZON[ind[1]]}")
        if self.__LAST_DIRECTION != 's': print(f"Go (s)outh towards {self.__HORIZON[ind[2]]}")
        if self.__LAST_DIRECTION != 'w': print(f"Go (w)est  towards {self.__HORIZON[ind[3]]}")

        while True:
            choice = input("Enter your choice: ")
            choice = choice.lower()
            if choice in ('n','e','s','w'):
                if choice == 'n': self.__LAST_DIRECTION = 's'
                if choice == 'e': self.__LAST_DIRECTION = 'w'
                if choice == 's': self.__LAST_DIRECTION = 'n'
                if choice == 'w': self.__LAST_DIRECTION = 'e'
                break


    def begin_adventure(self):

        while True:

            rand_death = random.randint(1,10)
            if self.day > 0 and rand_death == self.__RANDEAD:
                death_str = random.choice(self.__DEATHEVENT)
                print(f"\nOh dear! It seems {death_str}")
                print(f"Rest in Peace {self.name}...\n")
                break
            
            self.__print_directions()

            self.day+=1


if __name__ == '__main__':

    adventure = TextAdventure()
    adventure.begin_adventure()

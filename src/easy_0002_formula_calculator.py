'''
Ezra S. Brooker
Date Created: 2021-07-01

https://www.reddit.com/r/dailyprogrammer/comments/pjbj8/easy_challenge_2/

Hello, coders! An important part of programming is being able to apply 
your programs, so your challenge for today is to create a calculator 
application that has use in your life. It might be an interest calculator, 
or it might be something that you can use in the classroom. For example, 
if you were in physics class, you might want to make a F = M * A calc.

EXTRA CREDIT: make the calculator have multiple functions! Not only should 
it be able to calculate F = M * A, but also A = F/M, and M = F/A!

'''

import sys
if sys.version[0] != '3':
    raise Exception("Python 2 is no longer supported, please use Python 3")


class Calculator:
    ''' 
    Simple console calculator class that currently only supports kinetic
    energy calculations, can be expanded to other equations and support a 
    menu style approach through the console. (This can also be made into a
    proper GUI and done simply through PySimpleGUI.)
    '''

    def kineticEnergy(self):
        ''' Ek = 1/2 * m * v**2 '''
        
        print("Input known quantities, press <enter> to skip unknown quantity")
        m  = input("Mass: ")
        v  = input("Velocity: ")
        Ek = input("Kinetic energy: ")

        if len(m) == 0:
            m = 2.0*float(Ek) / float(v)**2
            print(f"\nCalulcated Mass = {m:2.8e} kg\n")

        elif len(v) == 0:
            v = (2.0*float(Ek) / float(m))**(0.5)
            print(f"\nCalulcated Velocity = {v:2.8e} ms/\n")

        elif len(Ek) == 0:
            Ek  = 0.5 * float(m) * float(v)**2
            print(f"\nCalulcated Kinetic energy = {Ek:2.2e} J\n")

        else:
            print("Nothing to calculate, all variable quanities are known")

if __name__ == '__main__':

    calc = Calculator()
    calc.kineticEnergy()

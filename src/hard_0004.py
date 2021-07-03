'''
Ezra S. Brooker
Date Created: 2021-07-02

Today, your challenge is to create a program that will take a series of numbers (5, 3, 15), 
and find how those numbers can add, subtract, multiply, or divide in various ways to relate
to each other. This string of numbers should result in 5 * 3 = 15, or 15 /3 = 5, or 15/5 = 3. 
When you are done, test your numbers with the following strings:

4, 2, 8

6, 2, 12

6, 2, 3

9, 12, 108

4, 16, 64

For extra credit, have the program list all possible combinations.

For even more extra credit, allow the program to deal with strings of greater than three numbers. 
For example, an input of (3, 5, 5, 3) would be 3 * 5 = 15, 15/5 = 3. When you are finished, test 
them with the following strings.

2, 4, 6, 3

1, 1, 2, 3

4, 4, 3, 4

8, 4, 3, 6

9, 3, 1, 7

'''

import sys
if sys.version[0] != '3':
    raise Exception("Python 2 is no longer supported, please use Python 3")

from itertools import permutations

class MathRelations:

    __relations = []
    __checked   = False
    __invalid   = False

    def __init__(self, number_string = "3 5 15 9"):
        self.set_numbers(number_string)


    def set_numbers(self, number_string):
        self.__numstr  = number_string
        self.__numbers = [n.replace(',','') for n in self.__numstr.strip().split()]
        self.__numlen  = len(self.__numbers)
        self.__checked = False
        self.__invalid = False
        self.__relations = []

    def get_numbers(self):
        return self.__numbers


    def __check_relations(self):

        if self.__numlen < 3:
            self.__invalid = True
            self.__relations = []
            return

        self.__relations = [self.__check(perm) for perm in permutations(self.__numbers)]
        self.__relations = set([rel for rel in self.__relations if rel is not None])
        self.__checked   = True


    def print_relations(self,number_string=None, logging=False):

        if number_string is not None:
            self.set_numbers(number_string)

        if not self.__checked:
            self.__check_relations()

        if len(self.__relations) > 0:
            print(f"\nThe numbers {self.__numstr} are related by")
            [print(rel) for rel in self.__relations]

        elif self.__invalid:
            print(f"\n[Warning] {self.__numstr} are not enough numbers to make relations\n")

        else:
            print(f"\nThe numbers {self.__numstr} have no relations")
        print("")


        if logging == True:
            self.log_relations()

        elif type(logging) is str:
            self.log_relations(logging)
        else:
            print(f"[Logging Error] var(logging) must be set to True to use\n\
                                    default logfile name or set to str(filename)")


    def log_relations(self, logfile="../logs/hard_0004.log"):

        with open(logfile,"a") as fout:
            if len(self.__relations) > 0:
                fout.write(f"\nNumbers {self.__numstr} are related by\n")
                [fout.write(f"{rel}\n") for rel in self.__relations]

            elif self.__invalid:
                fout.write(f"\n[Warning] {self.__numstr} are not enough numbers to make relations\n")

            else:
                fout.write(f"\nNumbers {self.__numstr} have no relations\n")


    def __check(self, nums):

        # Check for addition
        eqn = f"{nums[0]} + {nums[1]}"
        ans = f"{nums[2]}"        
        if eval(eqn) == eval(ans):
            return f"{eqn} = {ans}"

        # Check for substraction
        eqn = eqn.replace('+','-')
        if eval(eqn) == eval(ans):
            return f"{eqn} = {ans}"

        # Check for multiplication
        eqn = eqn.replace('-','*')
        if eval(eqn) == eval(ans):
            return f"{eqn} = {ans}"

        # Check for division
        eqn = eqn.replace('*','/')
        if eval(eqn) == eval(ans):
            return f"{eqn} = {ans}"

        # Check for modulo
        eqn = eqn.replace('/','%')
        if eval(eqn) == eval(ans):
            return f"{eqn} = {ans}"

        # Check for exponentiation
        eqn = eqn.replace('%','**')
        if eval(eqn) == eval(ans):
            return f"{eqn} = {ans}"



def test_01():
    
    numstrs = [
        "3, 5, 15",
        "4, 2, 8", 
        "6, 2, 12", 
        "6, 2, 3", 
        "9, 12, 108", 
        "4, 16, 64"
    ]

    MR = MathRelations()
    for nums in numstrs:
        MR.print_relations(nums, logging=True)


def test_02():

    numstrs = [
        "2, 4, 6, 3",
        "3, 5, 15, 3",
        "1, 1, 2, 3",
        "4, 4, 3, 4",
        "8, 4, 3, 6",
        "9, 3, 1, 7",
        "2, 3, 8, 4",
        "12, 4"
    ]

    MR = MathRelations()
    for nums in numstrs:
        MR.print_relations(nums, logging=True)


if __name__ == '__main__':

    test_01()
    test_02()

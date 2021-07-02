'''
Ezra S. Brooker
2021

Source: reddit.com/r/DailyProgrammer 2012-02-10
https://www.reddit.com/r/dailyprogrammer/comments/pih8x/easy_challenge_1/


Create a program that will ask the users name, age, and reddit username. have it tell them the information back, in the format:

        your name is (blank), you are (blank) years old, and your username is (blank)

for extra credit, have the program log this information in a file to be accessed later.

'''
import sys
if sys.version[0] != '3':
    raise Exception("Python 2 is no longer supported, please use Python 3")

def RedditInfo():
    name   = input("\n Hello Reddit user!\n What is your name?: ")
    age    = input(" What about your age?: ")
    user   = input(" And your Reddit username?: ")
    string = f"Your name is {name}, you are {age} years old, and your Reddit username is {user}\n"
    print(string)

    with open("./logs/easy_0001_reddit_users.log", 'w') as f_log:
        f_log.write(string)

if __name__ == '__main__':

    RedditInfo()

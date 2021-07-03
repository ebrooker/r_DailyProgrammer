'''
Ezra S. Brooker
Date Created: 2021-07-01

https://www.reddit.com/r/dailyprogrammer/comments/pjsdx/difficult_challenge_2/

Your mission is to create a stopwatch program.
This program should have start, stop, and lap options, 
and it should write out to a file to be viewed later.

'''

import sys
if sys.version[0] != '3':
    raise Exception("Python 2 is no longer supported, please use Python 3")
import time
import datetime

class StopWatch:

    def __init__(self):

        self.__time = 0.0
        self.__tlap = 0.0
        self.__nlap = 0
        self.__mode = -1

    def run(self):

        while True:
            choice = 0
            date = datetime.date.today()
            print(f"\n{date}: time = {self.__time:.2f}s   laptime = {self.__tlap}s   laps = {self.__nlap}")
            print("Choose an option:")
            print("    1. Start")
            print("    2. Stop ")
            print("    3. Lap  ")
            print("    4. Reset")
            print("    5. Log  ")
            print("    6. Exit  ")
            while choice not in [1,2,3,4,5,6]:
                choice = int(input("Enter here: "))
                if self.__mode == 1: self.__time = (time.time() - self.__tstart)/60.0
                
            if choice == 1:
                self.__start()

            elif choice == 2:
                self.__stop()
            
            elif choice == 3:
                self.__setlap()

            elif choice == 4:
                self.__reset()

            elif choice == 5:
                self.__log()

            elif choice == 6:
                break


    def __setlap(self):
        if self.__mode == 1: return
        self.__tlap = float(input("Enter lap time (MM.SS): "))


    def __lap(self):
        if self.__mode != 1: return
        self.__nlap = int(self.__time // self.__tlap)


    def __start(self):
        if self.__mode == 1: return
        self.__tstart = time.time()
        self.__mode = 1


    def __stop(self):
        if self.__mode != 1: return
        self.__time = (time.time() - self.__tstart) / 60.0
        self.__mode = 0

    def __reset(self):
        self.__tstart = 0.0
        self.__time   = 0.0
        self.__tlap   = 0.0
        self.__nlap   = 0
        self.__mode   = 0


    def __log(self):
        if self.__time > 0.0:
            with open("../logs/hard_0002_stopwatch.log","a") as fout:
                date = datetime.date.today()
                self.__lap()
                fout.write(f"{date}: time = {self.__time:.2f}s   laptime = {self.__tlap}s   laps = {self.__nlap}\n")


if __name__ == '__main__':

    watch = StopWatch()
    watch.run()
    
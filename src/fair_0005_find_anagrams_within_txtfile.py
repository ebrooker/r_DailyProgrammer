'''
Ezra S. Brooker
Date Created: 2021-07-03

https://www.reddit.com/r/dailyprogrammer/comments/pnhtj/2132012_challenge_5_intermediate/

Your challenge today is to write a program that can find the number of 
anagrams within a .txt file. 

For example, "snap" would be an anagram of "pans", and "skate" would be 
an anagram of "stake".

'''

import sys
if sys.version[0] != '3':
    raise Exception("Python 2 is no longer supported, please use Python 3")

from collections import Counter

from IPython import embed

def main():

    print("\nWelcome to the Anagram Searching Program (ASP)\n")

    fn = input("Enter textfile name to search: ")
    with open(fn, "r") as fin:
        lines   = fin.readlines()

    lines = [line.replace(',','').replace('\'','').replace('.','') for line in lines]
    words = [line.split() for line in lines]
    words = list(set(word.lower() for word in words[0] if len(word) > 1))
    sorts = [''.join(w for w in sorted(word)) for word in words]
    nanas = [v for v in Counter(sorts).values() if v > 1]
    sanas = int(sum(nanas))
    print(f"\n{fn} contains {sanas} anagrams\n")

if __name__ == '__main__':

    main()

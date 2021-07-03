'''
Ezra S. Brooker
Date Created: 2021-07-02

Welcome to cipher day!

For this challenge, you need to write a program that will take the scrambled words from this post, 
and compare them against THIS WORD LIST to unscramble them. For bonus points, sort the words by 
length when you are finished. Post your programs and/or subroutines!

(Word list can be found in ../data/hard_0003_wordlist.dat)

Here are your words to de-scramble:

mkeart

sleewa

edcudls

iragoge

usrlsle

nalraoci

nsdeuto

amrhat

inknsy

iferkna

'''

import sys
if sys.version[0] != '3':
    raise Exception("Python 2 is no longer supported, please use Python 3")

if __name__ == '__main__':

    from time import perf_counter

    scrambled = "mkeart sleewa edcudls iragoge usrlsle nalraoci nsdeuto amrhat inknsy iferkna".split()
    with open("../data/hard_0003_wordlist.dat","r") as fin:
        wordlist = [line.strip() for line in fin.readlines()]

    # Method 1:
    ti1 = perf_counter()
    hamlist     = [ ''.join(h for h in sorted(ham))  for ham  in wordlist                  ]
    scrambles   = [ ''.join(e for e in sorted(eggs)) for eggs in sorted(scrambled,key=len) ]
    unscrambled = [ ''.join(wordlist[hamlist.index(eggs)]) for eggs in scrambles           ]
    tf1 = perf_counter() - ti1
    print("".join(f"{eggs}\n" for eggs in unscrambled))


    # Method 2: (Adapted from method 2 to be a 1-liner, well, technically 2-liner including print statement)
    ti2 = perf_counter()
    unscrambled = [ [ham for ham in wordlist if sorted(ham) == sorted(eggs)] for eggs in sorted(scrambled,key=len) ]
    tf2 = perf_counter()-ti2
    print("".join(f"{eggs[0]}\n" for eggs in unscrambled))


    # Method 3: (Source: reddit user u/lnxaddct)
    ti3 = perf_counter()
    for eggs in sorted(scrambled, key=len):
        matches = [word for word in wordlist if sorted(eggs) == sorted(word)]
        print(''.join(matches))
    tf3 = perf_counter() - ti3


    print("\n#------- CPU Time -------#")
    print(f"#  Method 1: {tf1:2.7f}s  #")
    print(f"#  Method 2: {tf2:2.7f}s  #")
    print(f"#  Method 3: {tf3:2.7f}s  #")
    print("#------------------------#\n")
    
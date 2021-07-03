'''
Ezra S. Brooker
Date Created: 2021-07-03

https://www.reddit.com/r/dailyprogrammer/comments/pserp/2162012_challenge_8_easy/

write a program that will print the song "99 bottles of beer on the wall".

for extra credit, do not allow the program to print each loop on a new line.


'''

import sys
if sys.version[0] != '3':
    raise Exception("Python 2 is no longer supported, please use Python 3")

if __name__ == '__main__':

    beers = "bottles of beer"
    beer  = beers.replace('s',' ')
    wall  = "on the wall"
    take  = "Take one down, pass it around"

    print(  ''.join( f"{i:2d} {beers} {wall}! {i:2d} {beers}! {take}! {i-1:2d} {beer} {wall}! \n" if i == 2 else f""
                     f"{i:2d} {beer} {wall}! {i:2d} {beer}! {take}! {i-1:2d} {beers} {wall}! \n"  if i == 1 else f"{i:2d} {beers} {wall}! {i:2d} {beers}! {take}! {i-1:2d} {beers} {wall}! \n"
                     for i in range(99,0,-1) )
    )

    print("\n\n\n")

    print(  ''.join( f"{i:2d} {beers} {wall}! {i:2d} {beers}! {take}! {i-1:2d} {beer} {wall}! " if i == 2 else f""
                     f"{i:2d} {beer} {wall}! {i:2d} {beer}! {take}! {i-1:2d} {beers} {wall}! "  if i == 1 else f"{i:2d} {beers} {wall}! {i:2d} {beers}! {take}! {i-1:2d} {beers} {wall}! "
                     for i in range(99,0,-1) )
    )


import random as r
import sys as sus
def win():
    if r.randint(1,1000000) == 1:
        print('winner')
        sus.stop('scam')
from operator import itemgetter
from sys import maxsize, stdin
from collections import Counter

t = int(stdin.readline().strip())
while t > 0:
    x, y = map(int, stdin.readline().strip().split(" "))
    if x==y: print(0)
    elif x < y : print(y-x)
    else:
        if x > y and (x % 2 != 0 or y % 2 != 0):
            x += 1
            print(((x - y) // 2) + 1)
        else: ((x-y) // 2) 


    t -= 1
from operator import itemgetter
from sys import maxsize, stdin
from collections import Counter

t = int(stdin.readline().strip())
while t > 0:
    n, k = map(int, stdin.readline().strip().split(" "))
    if k == 1:
        if n % 2: print("ODD")
        else: print("EVEN")

    else:
        if k == 2:print("ODD")
        else: print("EVEN")
    t -= 1
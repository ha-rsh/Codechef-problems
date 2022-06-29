from operator import itemgetter
from sys import maxsize, stdin
from collections import Counter

t = int(stdin.readline().strip())
while t > 0:
    a, b , c = map(int, stdin.readline().strip().split(" "))
    if (a > b+c) or  (b > a+c) or (c > a+b):print("Yes")
    else: print("No")
    t -= 1
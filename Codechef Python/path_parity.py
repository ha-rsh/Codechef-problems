from operator import itemgetter
from sys import maxsize, stdin
from collections import Counter

t = int(stdin.readline().strip())
while t > 0:
    n, k = map(int, stdin.readline().strip().split(" "))
    if n % 2 == 0: print("yes")
    else:
        if k % 2 == 0: print("No")
        else: print("Yes")

    t -= 1
from operator import itemgetter
from sys import stdin
from collections import Counter

t = int(stdin.readline().strip())
while t > 0:
    n = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().strip().split(' ')))
    count = 0
    for i in arr:
        if i == 0: count += 1

    if count <= n//2: print(1)
    else: print(0)
    t -= 1

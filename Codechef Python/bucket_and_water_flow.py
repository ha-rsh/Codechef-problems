from operator import itemgetter
from sys import maxsize, stdin
from collections import Counter

t = int(stdin.readline().strip())
while t > 0:
    w, x, y, z = map(int, stdin.readline().strip().split(" "))
    if ((y * z) + w) == x: print("Filled")
    elif ((y * z) + w) > x: print("Overflow")
    else: print("Unfilled")
    t -= 1
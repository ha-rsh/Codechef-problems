from operator import itemgetter
from sys import maxsize, stdin
from collections import Counter

t = int(stdin.readline().strip())
while t > 0:
    n, x = map(int, stdin.readline().strip().split(" "))
    arr_s = list(map(int, stdin.readline().strip().split(" ")))
    arr_s.sort()
    if arr_s[0] > x or arr_s[n-1] < x: print("No")
    else: print("Yes")
    t -= 1

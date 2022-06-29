from cgitb import reset
from operator import itemgetter
from re import L
from sys import stdin
from collections import Counter

t = int(stdin.readline().strip())
while t > 0:
    n = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().strip().split(' ')))
    result = 0
    for i in arr: result += i
    result *= 2
    if result % n == 0 and ((result // n) % 2 == 1): print("Yes")
    else: print("No")
    t -= 1

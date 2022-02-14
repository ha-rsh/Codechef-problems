from sys import stdin
from traceback import print_tb

t = int(stdin.readline().strip())
while t > 0:
    a, b, c = list(map(int, stdin.readline().strip().split(' ')))
    if a + b == c or b + c == a or a + c == b: print("Yes")
    else:print("No")
    t -= 1

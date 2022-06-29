from operator import itemgetter
from sys import maxsize, stdin
from collections import Counter

t = int(stdin.readline().strip())
while t > 0:
    a, b = map(int, stdin.readline().strip().split(" "))
    op = 0
    if a % 3 == 0 or b % 3 == 0: op = 0
    else:
        while True:
            a = abs(a - b)  
            op += 1
            if a % 3 == 0: break

    print(op)
    t -= 1
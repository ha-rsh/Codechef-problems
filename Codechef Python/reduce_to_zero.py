from operator import itemgetter
from sys import maxsize, stdin
from collections import Counter, defaultdict

t = int(stdin.readline().strip())
while t > 0:
    x, y = map(int, stdin.readline().strip().split(" "))
    res = 0
    if x > y: x , y = y , x
    if x == 0 and y == 0: print(0)
    elif x == 0 and y != 0: print(-1)
    elif x != 0 and y != 0:
        while x < y: 
            res += 1
            x *= 2
            print(f"x: {x}")

        print(res + y)

    t -= 1
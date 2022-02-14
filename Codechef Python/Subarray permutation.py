from sys import stdin
from traceback import print_tb

t = int(stdin.readline().strip())
while t > 0:
    n, k = list(map(int, stdin.readline().strip().split(' ')))
    if k < 2 and n != 1:
        print(-1)
    else:
        for i in range(k, n+1):
            print(i, end=" ")
        for i in range(1, k):
            print(i, end=" ")
        print()

    t -= 1

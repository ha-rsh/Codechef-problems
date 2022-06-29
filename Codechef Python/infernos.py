from operator import itemgetter
from sys import maxsize, stdin
from collections import Counter

t = int(stdin.readline().strip())
while t > 0:
    n, x = map(int, stdin.readline().strip().split(" "))
    arr = list(map(int, stdin.readline().strip().split(' ')))
    temp = -maxsize
    count = 0
    for i in range(n):
        temp=max(temp, arr[i])
        count += (arr[i] // x)
        if arr[i] % x:count += 1

    print(min(count, temp))
    t -= 1
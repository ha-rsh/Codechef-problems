from cgitb import reset
from sys import stdin

t = int(stdin.readline().strip())
while t > 0:
    n, x = map(int, stdin.readline().strip().split(' '))
    nums = list(map(int, stdin.readline().strip().split(' ')))
    result = 0
    for i in range(n):
        if nums[i] < x:
           result = i + 1

    print(result)

    t -= 1
    
from sys import stdin

t = int(stdin.readline().rstrip())
while t > 0:
    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().strip().split(' ')))
    maximum = max(arr)
    minimum = min(arr)
    print(maximum-minimum)
    t -= 1
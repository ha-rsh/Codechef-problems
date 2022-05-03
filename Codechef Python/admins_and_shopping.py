from sys import stdin
import math

t = int(stdin.readline().strip())
while t > 0:
    shops, admins = map(int, stdin.readline().strip().split(' '))
    capacity = list(map(int, stdin.readline().strip().split(' ')))
    minimum = min(capacity)
    result = max(shops, math.ceil(admins / minimum))
    print(result)
    t -= 1

from sys import stdin
import math

t = int(stdin.readline().rstrip())
while t > 0:
    n = int(stdin.readline().strip())
    value = pow((0.143 * n), n)
    if (value - math.floor(value)) < 0.5:
        print(math.floor(value))

    else:print(int(value) + 1)
    t -= 1

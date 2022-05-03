from sys import stdin

t = int(stdin.readline().strip())
while t > 0:
    n = int(stdin.readline().strip())
    if n == 1: print(1)
    elif n >= 2 and n <= 4: print(n-1)
    else: print(n)
    t -= 1
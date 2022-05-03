from sys import stdin

t = int(stdin.readline().strip())
while t > 0:
    k, x = map(int, stdin.readline().strip().split(' '))
    print(k-x)
    t -= 1
    
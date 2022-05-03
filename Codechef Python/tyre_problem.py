from sys import stdin

t = int(stdin.readline().strip())
while t > 0:
    n, m = map(int, stdin.readline().strip().split(' '))
    tyres = (2 * n) + (4 * m)
    print(tyres)
    t -= 1
    
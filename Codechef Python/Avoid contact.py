from sys import stdin

t = int(stdin.readline().rstrip())
while t > 0:
    x, y = list(map(int, stdin.readline().strip().split(' ')))
    if y == 0:
        print(x)

    elif x == y:
        print(2*y-1)

    else:
        print((x-y)+2*y)

    t -= 1
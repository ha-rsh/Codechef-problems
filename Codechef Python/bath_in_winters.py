from sys import stdin

t = int(stdin.readline().strip())
while t > 0:
    x, y = map(int, stdin.readline().strip().split(' '))
    ans = x // (2 * y)
    print(ans)
    t -= 1
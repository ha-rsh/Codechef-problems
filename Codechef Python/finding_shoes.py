from sys import stdin

t = int(stdin.readline().strip())
while t > 0:
    n, m = map(int, stdin.readline().strip().split(' '))
    if m >= n: print(n)
    else:
       diff = abs(m - n)
       print(n + diff)
    t -= 1
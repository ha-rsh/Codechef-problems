from sys import stdin

t = int(stdin.readline().rstrip())
while t > 0:
    x, y, k = map(int, stdin.readline().strip().split(' '))
    if k == 1:
        print('YES')

    elif x % k == 0 and y % k == 0:
        print('YES')

    else:
        print('NO')
        
    t -= 1
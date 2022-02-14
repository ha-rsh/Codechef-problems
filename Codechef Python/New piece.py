from sys import stdin

t = int(stdin.readline().rstrip())
while t > 0:
    a,b,p,q = map(int, stdin.readline().strip().split(' '))

    s = abs(a-p)+abs(b-q)
    if s:
        if s%2 ==0:
            print(2)
        else:
            print(1)
    else:
        print(0)

    t -= 1

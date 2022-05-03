from sys import stdin

t = int(stdin.readline().strip())
while t > 0:
    x,y,z = map(int, stdin.readline().strip().split(' '))
    if x + y <= z: print(2)
    elif x < z:print(0)
    else: print(1)
    t -= 1
from sys import stdin

t = int(stdin.readline().strip())
while t > 0:
    x, y = map(int, stdin.readline().strip().split(' '))
    if x > y: print("CAR")
    elif x == y: print("SAME")
    else: print("BIKE")
    t -= 1
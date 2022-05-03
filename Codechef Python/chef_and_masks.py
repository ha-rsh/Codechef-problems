from sys import stdin

t = int(stdin.readline().strip())
while t > 0:
    x,y = map(int, stdin.readline().strip().split(' '))
    if x * 100 < y * 10: print("Disposable")
    elif x * 100 == y * 10 : print("Cloth")
    else: print("Cloth")
    t-=1

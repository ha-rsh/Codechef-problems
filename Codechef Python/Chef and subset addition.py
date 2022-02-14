from sys import stdin

t = int(stdin.readline().strip())
while t > 0:
    n, x, y = list(map(int, stdin.readline().strip().split(' ')))
    a = list(map(int, stdin.readline().strip().split(' ')))
    b = list(map(int, stdin.readline().strip().split(' ')))
    count = 0
    for i in range(len(a)):
        if a[i] + x == b[i]:
            count += 1

        elif a[i] + y == b[i]:
            count += 1


    if count == len(a):
        print("Yes")
        
    else:
        print("No")

    t -= 1

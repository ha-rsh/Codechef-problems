from sys import stdin

t = int(stdin.readline().rstrip())
while t > 0:
    n = int(stdin.readline().rstrip())
    arr = []
    p = 1
    for i in range(n):
        arr.append(p)
        p += 2

    for i in range(n):
        print(arr[i], end=" ")

    print()
    t -= 1
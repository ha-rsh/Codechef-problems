from sys import stdin

t = int(stdin.readline().strip())
while t > 0:
    n = int(stdin.readline().strip())
    if n % 2:
        if n == 1 or n == 3:
            print(-1)
        else:
            print("3 5 1 2 4 ")
            for i in range(n, 5, -1):
                print(i, end=" ")
            print()

    else:
        for i in range(1, n + 1):
            print(n+1-i, end=" ")
        print()
    t -= 1
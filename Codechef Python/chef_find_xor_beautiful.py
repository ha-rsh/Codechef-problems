from sys import stdin

t = int(stdin.readline().strip())
while t > 0:
    n = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().strip().split(' ')))
    x = int(stdin.readline().strip())
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] ^ arr[j]) & x == 0:
                count += 2

    for i in range(n):
        if (arr[i] ^ arr[i]) & x == 0:
            count += 1
    print(count)
    t -= 1

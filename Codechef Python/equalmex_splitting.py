from sys import stdin

t = int(stdin.readline().strip())
while t > 0:
    n = int(stdin.readline().strip())
    nums = list(map(int, stdin.readline().strip().split()))
    c = 0
    for i in nums:
        if i == 0:
            c += 1

    print(max(c, n-c))
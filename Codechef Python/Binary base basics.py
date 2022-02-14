from sys import stdin

t = int(stdin.readline().rstrip())
while t > 0:
    n, k = map(int, stdin.readline().strip().split(' '))
    s = stdin.readline().strip()[:n]
    j = n - 1
    i = 0
    op = 0
    while i < j:
        if s[i] != s[j]:
            op += 1

        i += 1
        j -= 1
    
    if op <= k:
        if n % 2 == 1: print("YES")
        elif (k - op) % 2 == 0:print("YES")
        else:print("NO")

    else: print("NO")
    t -= 1


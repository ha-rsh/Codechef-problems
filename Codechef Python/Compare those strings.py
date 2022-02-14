from sys import stdin

t = int(stdin.readline().rstrip())
while t > 0:
    n = int(stdin.readline().rstrip())
    a = stdin.readline().rstrip()
    b = stdin.readline().rstrip()
    ans = 0
    flag = b[n-1] > a[n-1]
    if flag:
        ans += 1

    for i in range(n-2,-1,-1):
        if b[i] > a[i]:
            flag = True
            ans += 1
        elif b[i] < a[i]:
            flag = False
        else:
            if flag:
                ans += 1

    print(ans)
    t -= 1

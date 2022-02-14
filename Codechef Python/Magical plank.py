from sys import stdin

t = int(stdin.readline().rstrip())
while t > 0:
    n = int(stdin.readline().strip())
    s = stdin.readline().rstrip()
    count = 0
    for i in range(n-1):
        if s[i] != s[i+1]:
            count += 1

    print((count+1)//2)
    t -= 1
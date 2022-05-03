from sys import stdin

t = int(stdin.readline().strip())
while t > 0:
    n = int(stdin.readline().strip())
    s = stdin.readline().strip()
    count = 1
    for i in range(1, len(s)):
        if s[i - 1] != s[i]:
           count += 1

    print(count)
    t -= 1
        
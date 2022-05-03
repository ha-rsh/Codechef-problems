from sys import stdin

t = int(stdin.readline().strip())
while t > 0:
    n = int(stdin.readline().strip())
    s = stdin.readline().strip()
    s += "1"
    op = 0
    i = 0
    while i < n:
        if s[i]==s[i+1]:
            op += 1
            i += 2
          
        else:
            op += 1
        i += 1

    print(op)
    t -= 1



from sys import stdin
from collections import Counter

t = int(stdin.readline().strip())
while t > 0:
    a, b = map(str, stdin.readline().strip().split(' '))
    n = int(stdin.readline().strip())
    p = a + b
    c = ""
    for i in range(n):
        c += stdin.readline().strip()

    freq = Counter(p)
    flag = True
    for i in c:
        if freq[i] > 0: freq[i] -= 1
        else: 
            flag = False
            break
        

    print("YES") if flag else print("NO")
    t -= 1
    
from operator import itemgetter
from sys import maxsize, stdin
from collections import Counter

t = int(stdin.readline().strip())
while t > 0:
    n = int(stdin.readline().strip())
    a = list(map(int, stdin.readline().strip().split(" ")))
    b = list(map(int, stdin.readline().strip().split(" ")))
    ans = 0
    my_dict = {}
    for i in range(n):
        try:ans += my_dict[(a[i], b[i])]
        except: pass
        if (b[i], a[i]) in my_dict: my_dict[(b[i], a[i])] += 1
        else: my_dict[(b[i], a[i])] = 1

    print(ans)
    t -= 1
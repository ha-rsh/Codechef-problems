from operator import itemgetter
from sys import maxsize, stdin
from collections import Counter, defaultdict
from math import log

t = int(stdin.readline().strip())
while t > 0:
    a, b, n = map(int, stdin.readline().strip().split(" "))
    if a == b: print(0)
    else:
        if (a^b) < n:print(1)
        else:
            if int(log((a^b),2)) == int(log(n,2)):
                if n &(n-1):print(2)
                else: print(-1)

            else:print(-1)
            
    t -= 1
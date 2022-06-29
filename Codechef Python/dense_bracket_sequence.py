from operator import itemgetter
from sys import maxsize, stdin
from collections import Counter, defaultdict
from math import log

t = int(stdin.readline().strip())
while t > 0:
    n = int(stdin.readline().strip())
    s = stdin.readline().strip()
    op = 0
    i = 0
    j = len(s) - 1
    while j > i:
        if s[i] == "(" and s[j] == ")":
           i += 1
           j -= 1
        
        elif s[i] == '(' and s[j] == '(':
           j -= 1
           op += 1

        elif s[i] == ")" and s[j] == "(":
            j -= 1
            op += 1

        elif s[i] == ")" and s[j] == ")":
            i += 1
            op += 1

    print(op)
    t -= 1

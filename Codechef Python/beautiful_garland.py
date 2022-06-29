from operator import itemgetter
from sys import maxsize, stdin
from collections import Counter, defaultdict

t = int(stdin.readline().strip())
while t > 0:
    s = stdin.readline().strip()
    rr_count = 0
    gg_count = 0
    for i in range(len(s)):
        if s[i - 1] == "R" and s[i] == "R": rr_count += 1
        elif s[i - 1] == "G" and s[i] == "G" : gg_count += 1

    if rr_count == 0 and gg_count == 0: print("yes")
    elif rr_count == 1 and gg_count == 1: print("yes")
    else: print("no") 
    t -= 1
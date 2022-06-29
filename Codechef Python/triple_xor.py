from operator import itemgetter
from sys import maxsize, stdin
from collections import Counter, defaultdict
from math import log

t = int(stdin.readline().strip())
while t > 0:
    n, k = map(int, stdin.readline().strip().split(" "))
    temp = pow(2 , n) - 1
    print(temp*(temp - 1))
    t -= 1
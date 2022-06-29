from operator import itemgetter
from sys import maxsize, stdin
from collections import Counter

t = int(stdin.readline().strip())
while t > 0:
    a, b , m = map(int, stdin.readline().strip().split(" "))
    min_dis1 = abs(a-b)
    min_dis2 = abs(m - min_dis1)

    print(min(min_dis1, min_dis2))
    t -= 1
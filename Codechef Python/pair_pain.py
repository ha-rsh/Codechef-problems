from sys import stdin
from collections import Counter

t = int(stdin.readline().strip())
while t > 0:
    n = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().strip().split(' ')))
    one_count, two_count = 0, 0
    for i in arr:
        if i == 1: one_count += 1
        elif i == 2: two_count += 1

    val = (one_count * (n - one_count))
    if one_count > 1:
        val += ((one_count * (one_count - 1)) // 2)
 
    if two_count > 1:
        val += ((two_count * (two_count - 1)) // 2)
 
    print(val)
    t -= 1

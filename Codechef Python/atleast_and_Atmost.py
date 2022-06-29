from operator import itemgetter
from sys import maxsize, stdin
from collections import Counter, defaultdict
from math import log
import ctypes
import itertools

t = int(stdin.readline().strip())
while t > 0:
    n = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    temp1 = [0] * (n+1)
    temp2 = [0] * (n+1)
    temp3 = [0] * (n+1)
    temp1[:] = itertools.repeat(0, len(temp1))
    temp2[:] = itertools.repeat(0, len(temp2))
    temp3[:] = itertools.repeat(0, len(temp3))
    for i in range(n):
        temp1[0] += 1
        temp1[arr[i]] -= 1
        temp2[0] += (n - arr[i] + 1)
        temp2[arr[i]] -= (n - arr[i] + 1) 
        temp3[n - 1] += (n - arr[i]) 
        temp3[arr[i]] -= (n - arr[i])

    for i in range(1, n+1):
        temp1[i] += temp1[i-1]
        temp2[i] += temp2[i-1]
    
    for i in range(n-2, -1, -1):
        temp3[i] += temp3[i + 1]

    for i in range(n):
        print(temp1[i], temp2[i] + temp3[i])


    t -= 1
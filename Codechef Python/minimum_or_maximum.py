from operator import itemgetter
from sys import maxsize, stdin
from collections import OrderedDict
from tkinter.messagebox import NO

from numpy import argsort

t = int(stdin.readline().strip())
while t > 0:
    n = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    curr_min = arr[0]
    curr_max = arr[0]
    flag = False
    for i in range(1, n):
        if arr[i] < curr_max and arr[i] > curr_min: 
            flag = True
            break

        curr_min = min(curr_min, arr[i])
        curr_max = max(curr_max, arr[i])

    if flag: print("No")
    else: print("Yes")
    t -= 1
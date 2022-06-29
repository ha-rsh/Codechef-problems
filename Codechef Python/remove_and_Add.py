from operator import itemgetter
from sys import maxsize, stdin
from collections import OrderedDict

t = int(stdin.readline().strip())
while t > 0:
    n = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    temp = n - 1
    res = n
    j = 0
    my_dict = OrderedDict()
    for i in range(n):
        my_dict[arr[i]] = 1 + i

    for i in range(n):
        temp = n - i - 1
        if list(my_dict.keys()).index(arr[i]) != len(my_dict) - 1:
            temp1 = my_dict[arr[i]]

        else: temp1 = 0
        j = max(temp1, j)
        res = min(res, min(j, temp) + j + temp)
    
    print(res)
    t -= 1

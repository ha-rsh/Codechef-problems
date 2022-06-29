from operator import itemgetter
from sys import stdin
from collections import Counter

t = int(stdin.readline().strip())
while t > 0:
    n = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().strip().split(' ')))
    freq = [0] * 11
    for i in range(len(arr)):
        freq[arr[i]] += 1

    temp = 0
    flag = 0
    for i in range(len(freq)):
        if freq[temp] < freq[i] :
            temp = i
            flag = 0
        elif freq[temp] == freq[i]:
            flag = 1
    if flag:
        print('Confused')
    else:
        print(temp)
    t -= 1
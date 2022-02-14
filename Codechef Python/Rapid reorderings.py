from sys import stdin
from collections import Counter


def check1(arr):
    new_dict = {}
    for i in range(len(arr)):
        temp = arr[:i+1]
        if len(temp) % 2 == 0:
            value = len(temp) // 2
            value -= 1
            median = arr[value]
        else:
            value = len(temp) // 2
            median = arr[value]

        if median not in new_dict:
            new_dict[median] = 1

        else:
            new_dict[median] += 1

    return new_dict


def check2(arr):
    new_dict = {}
    for i in range(len(arr)-1, -1, -1):
        temp = arr[i:]
        if len(temp) % 2 == 0:
            value = len(temp) // 2
            value -= 1
            median = temp[value]
        else:
            value = len(temp) // 2
            median = temp[value]

        if median not in new_dict:
            new_dict[median] = 1

        else:
            new_dict[median] += 1

    return new_dict


t = int(stdin.readline().rstrip())
while t > 0:
    n = int(stdin.readline().rstrip())
    b = list(map(int, stdin.readline().strip().split(' ')[:2*n]))
    my_dict = Counter(b)
    s = set(b)
    arr = list(s)
    arr.sort()
    dict1 = check1(arr)
    dict2 = check2(arr)
    l1 = [0] * (max(arr) + 1)
    for key, item in dict1.items():
        l1[key] += item

    for key, item in dict2.items():
        l1[key] += item

    flag = True
    for key, item in my_dict.items():
        if item == l1[key]:
            flag = True

        else:
            flag = False
            break

    if flag:
        print(*arr)

    else:
        print(-1)

    t -= 1
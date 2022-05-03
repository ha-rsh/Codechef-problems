from sys import stdin
from collections import Counter

t = int(stdin.readline().strip())
while t > 0:
    n = int(stdin.readline().strip())
    nums = list(map(int,stdin.readline().strip().split(' ')[:2*n]))
    my_dict = Counter(nums)
    flag = True

    for i in range(2*n):
        if my_dict[i] == 1:
            flag = False
            break

        elif my_dict[i] == 0:
            break

    if flag: print("Yes")
    else: print("No")

    t -= 1
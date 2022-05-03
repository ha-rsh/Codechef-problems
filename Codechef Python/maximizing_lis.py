import bisect
from sys import maxsize, stdin

def max_lis(nums: list, n:int):
    my_list = []
    ele = [0] * n
    for i in range(n):
        if not my_list:
           my_list.append(nums[i])
           ele[i] = len(my_list)
           continue
        val = bisect.bisect_left(my_list, nums[i])
        if val == len(my_list): my_list.append(nums[i])
        else: my_list[val] = nums[i]
        ele[i] = len(my_list)

    return ele



t = int(stdin.readline().strip())
while t > 0:
    n = int(stdin.readline().strip())
    nums = list(map(int, stdin.readline().strip().split(' ')))
    ans1 = max_lis(nums, n)
    for i in range(n):
        nums[i] = -nums[i]

    nums = nums[::-1]
    ans2 = max_lis(nums, n)
    ans2 = ans2[::-1]
    res = 0
    for i in range(n-1):
        res = max(res, ans1[i] + ans2[i+1])

    print(res)

    t -= 1



from sys import stdin

t = int(stdin.readline().rstrip())
while t > 0:
    n, k = map(int, stdin.readline().strip().split(' '))
    test = list(map(int, stdin.readline().strip().split(' ')))
    nums = []
    for i in range(len(test)):
        if i == 0:
            nums.append(test[i])

        elif test[i] != nums[-1]:
            nums.append(test[i])

    n = len(nums)
    totaluglines = 0
    for i in range(n-1):
        if nums[i] != nums[i + 1]:
            totaluglines += 1

    new_nums = [totaluglines] * (k + 1)
    for i in range(n):
        if i + 1 < n:
            new_nums[nums[i]] -= 1

        if i - 1 >= 0:
            new_nums[nums[i]] -= 1

        if (i-1) >= 0 and (i + 1) < n and nums[i + 1] != nums[i - 1]:
            new_nums[nums[i]] += 1

    for i in range(1, k + 1):
        print(new_nums[i], end=" ")
    print()
    t -= 1

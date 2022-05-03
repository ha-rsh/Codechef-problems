from sys import stdin

t = int(stdin.readline().rstrip())
while t > 0:
    n = int(stdin.readline().rstrip())
    nums = list(map(int, stdin.readline().strip().split(' ')[:n]))
    flag = True
    for i in range(1, n):
        if nums[i - 1] % nums[i] != 0:
            flag = False

    if flag:
        for i in range(n):
            print(nums[i], end=" ")
        print()

    else:
        print(-1)
    t -= 1
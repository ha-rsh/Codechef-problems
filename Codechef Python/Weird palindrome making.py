from sys import stdin

t = int(stdin.readline().rstrip())
while t > 0:
    n = int(stdin.readline().rstrip())
    nums = list(map(int, stdin.readline().strip().split(" ")[:n]))
    op = 0
    count = 0
    for i in range(len(nums)):
        if nums[i]%2 != 0:
            count += 1

    print(count//2)
    t -= 1
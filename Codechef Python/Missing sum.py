from sys import stdin

t = int(stdin.readline().rstrip())
while t > 0:
    n = int(stdin.readline().rstrip())
    nums = []
    p = 1
    for i in range(n):
        nums.append(p)
        p += 2

    for i in range(n):
        print(nums[i], end=" ")

    print()
    t -= 1
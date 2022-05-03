from sys import stdin

t = int(stdin.readline().rstrip())
while t > 0:
    n = int(stdin.readline().rstrip())
    nums = list(map(int, stdin.readline().strip().split(' ')))
    maximum = max(nums)
    minimum = min(nums)
    print(maximum-minimum)
    t -= 1
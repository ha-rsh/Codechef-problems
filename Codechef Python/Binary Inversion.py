from sys import stdin

t = int(stdin.readline().rstrip())
while t > 0:
    n, m = map(int, stdin.readline().rstrip().split(' '))
    nums = []
    for i in range(n):
        s = stdin.readline().strip()
        nums.append(s)

    nums.sort(key=lambda i: i.count('1'))
    nums = ''.join(nums)
    ones = 0
    inversions = 0
    for i in nums:
        if i == '1':
            ones += 1
        else:
            inversions += ones

    print(inversions)
    t -= 1

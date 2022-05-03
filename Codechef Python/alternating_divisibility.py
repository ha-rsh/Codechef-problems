from sys import stdin

def alternating(n):
    nums = [None] * n
    value = 1
    if n == 1:
        print(1)
        return

    for i in range(0, n-1, 2):
        nums[i] = value
        nums[i+1] = 2*value
        value += 2

    if n%2 != 0:
        nums[n-1] = nums[n-2] + 1

    for i in range(n):
        print(nums[i], end=" ")

    print()

t = int(stdin.readline().strip())
while t > 0:
    n = int(stdin.readline().strip())
    alternating(n)
    t -= 1


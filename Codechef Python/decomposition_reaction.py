from sys import stdin
mod = pow(10,9) + 7

n, m = map(int, stdin.readline().strip().split(' '))
nums = list(map(int, stdin.readline().strip().split(' ')))
for i in range(m):
    c, x = map(int, stdin.readline().strip().split(' '))
    u = list(map(int, stdin.readline().strip().split(' ')[:2*x]))
    aux = nums[c -1]
    nums[c - 1] = 0
    for i in range(0, len(u)-1, 2):
        nums[u[i + 1] - 1] = (nums[u[i + 1] - 1] + aux * u[i]) % mod

for i in nums:
    print(i)

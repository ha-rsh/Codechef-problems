from sys import stdin
mod = pow(10,9) + 7
n_max = pow(10,5) + 5

t = int(stdin.readline().strip())
while t > 0:
    n = int(stdin.readline().strip())
    nums = [0, 1]
    for i in range(2, n_max):
        nums.append((nums[i-1] * 2) % mod)

    print(nums[n])
    t -= 1

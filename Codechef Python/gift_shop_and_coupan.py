from sys import stdin

t = int(stdin.readline().strip())
while t > 0:
    n, k = map(int, stdin.readline().strip().split(' '))
    nums = list(map(int, stdin.readline().strip().split(' ')))
    nums.sort()
    ans = 0
    for i in range(len(nums)):
        if k >= nums[i]:
            ans += 1
            k -= nums[i]

        else:
            if (nums[i] // 2) + (nums[i] % 2) <= k:
                ans += 1

            break

    print(ans)
    t -= 1


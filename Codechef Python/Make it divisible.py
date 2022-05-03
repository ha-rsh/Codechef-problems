from sys import stdin

t = int(stdin.readline().rstrip())
while t > 0:
    n = int(stdin.readline().rstrip())
    nums = list(map(int, stdin.readline().strip().split(' ')))
    sum = 0
    mod0 = 0
    mod1 = 0
    mod2 = 0
    for i in range(n):
        if nums[i] % 3 == 1:
            mod1 += 1

        elif nums[i] % 3 == 2:
            mod2 += 1

    score = min(mod1, mod2)
    mod = max(mod1, mod2) - score
    if (mod % 3) == 0:
        score += 2*(mod/3)
    else:
        score = -1

    print(int(score))

    t -= 1
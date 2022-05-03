from sys import stdin, maxsize

t = int(stdin.readline().strip())
while t > 0:
    n , k = map(int, stdin.readline().strip().split(" "))
    nums = list(map(int, stdin.readline().strip().split(" ")))
    result = []
    start = 0
    en = 0
    for i in range(k):
        en = nums[i]
        while en > start:
            result.append(en)
            en -= 1

        start = nums[i]

    for i in range(n):
        print(result[i], end=" ")

    print()
    t -= 1
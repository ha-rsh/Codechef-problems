from sys import stdin

t = int(stdin.readline().rstrip())
while t > 0:
    n, k = map(int, stdin.readline().strip().split(' '))
    test = list(map(int, stdin.readline().strip().split(' ')))
    arr = []
    for i in range(len(test)):
        if i == 0:
            arr.append(test[i])

        elif test[i] != arr[-1]:
            arr.append(test[i])

    n = len(arr)
    totaluglines = 0
    for i in range(n-1):
        if arr[i] != arr[i + 1]:
            totaluglines += 1

    new_arr = [totaluglines] * (k + 1)
    for i in range(n):
        if i + 1 < n:
            new_arr[arr[i]] -= 1

        if i - 1 >= 0:
            new_arr[arr[i]] -= 1

        if (i-1) >= 0 and (i + 1) < n and arr[i + 1] != arr[i - 1]:
            new_arr[arr[i]] += 1

    for i in range(1, k + 1):
        print(new_arr[i], end=" ")
    print()
    t -= 1

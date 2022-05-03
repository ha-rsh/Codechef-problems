from sys import stdin

t = int(stdin.readline().strip())
while t > 0:
    n = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    arr.sort(reverse=True)
    for i in range(1, n-2):
        if ((arr[i] - arr [i-1]) == 2 * (arr[i+1] - arr[i])) or (2*(arr[i] - arr[i - 1]) == arr[i+1] - arr[i]):
            continue
        else:print("No")

    print("Yes")
    t -= 1
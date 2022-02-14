from sys import stdin

t = int(stdin.readline().rstrip())
while t > 0:
    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().strip().split(" ")[:n]))
    op = 0
    count = 0
    for i in range(len(arr)):
        if arr[i]%2 != 0:
            count += 1

    print(count//2)
    t -= 1
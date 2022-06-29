from operator import itemgetter
from sys import maxsize, stdin
from collections import Counter

t = int(stdin.readline().strip())
while t > 0:
    n, m = map(int, stdin.readline().strip().split(" "))
    arr = list(map(int, stdin.readline().strip().split(" ")))
    arr.sort()
    temp = []
    ans = -maxsize
    for i in range(n):
        temp.append((arr[i] - arr[n-1]) % m)
        ans = max(ans, temp[i] + arr[i] + arr[n-1])
    print(ans)
    t -= 1

from sys import stdin

def good_prefix(s, mid):
    operations = 0
    for i in range(mid-1 , -1, -1):
        req = (operations + int(s[i])) % 10
        if req != 0: operations += 10 - req

    return operations

def binary_search(s, low, high, k):
    while low < high:
        mid = low + ((high - low)//2)
        op = good_prefix(s, mid)
        if op <= k: low = mid + 1
        else: high = mid

    return low-1

t = int(stdin.readline().strip())
while t > 0:
    n, k = list(map(int, stdin.readline().strip().split(' ')))
    s = stdin.readline().strip()
    low = 0
    high = n + 1
    result = binary_search(s, low, high, k)
    print(result)

    t -= 1

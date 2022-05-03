from sys import stdin

t = int(stdin.readline().strip())
while t > 0:
    n, k = map(int, stdin.readline().strip().split(' '))
    n_arr = list(map(int, stdin.readline().strip().split(' ')))
    n_arr.sort()
    print(n_arr[min(k, n - 1)])
    t -= 1
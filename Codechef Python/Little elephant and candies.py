from sys import stdin

t = int(stdin.readline().strip())
while t > 0:
    n, c = list(map(int, stdin.readline().strip().split(' ')))
    arr = list(map(int, stdin.readline().strip().split(' ')))
    total = sum(arr)
    if total <= c: print("Yes") 
    else: print("No")
    t -= 1


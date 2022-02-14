from sys import stdin

t = int(stdin.readline().rstrip())
while t > 0:
    n, m = map(int, stdin.readline().rstrip().split(' '))
    arr = []
    for i in range(n):
        s = stdin.readline().strip()
        arr.append(s)

    arr.sort(key=lambda i: i.count('1'))
    arr = ''.join(arr)
    ones = 0
    inversions = 0
    for i in arr:
        if i == '1':
            ones += 1
        else:
            inversions += ones

    print(inversions)
    t -= 1

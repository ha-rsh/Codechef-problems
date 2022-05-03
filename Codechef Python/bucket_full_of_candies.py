from sys import stdin

t = int(stdin.readline().strip())
while t > 0:
    n, m, l = map(int, stdin.readline().strip().split(' '))
    last_bucket = l + (n - 1)
    while(m >= l and last_bucket >= l):
        val1 = m % last_bucket
        if val1 == m and m >= l:
           last_bucket = m
           m = val1
           continue
        else:
             m = val1
        last_bucket -= 1

    print(m)

    t -= 1

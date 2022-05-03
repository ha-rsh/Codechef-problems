from sys import stdin

t = int(stdin.readline().strip())
while t > 0:
    n, x, y = map(int, stdin.readline().strip().split(' '))
    string = stdin.readline().strip()
    string = list(string)
    if x <= y: string.sort()
    else: string.sort(reverse=True)
    string = "".join(string)
    count1 = 0
    count2 = 0
    count1 = string.count("01")
    count2 = string.count("10")
    print((count1 * x) + (count2 * y))
    t -= 1
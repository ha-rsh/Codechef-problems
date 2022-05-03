from sys import stdin

t = int(stdin.readline().strip())
while t > 0:
    n = int(stdin.readline().strip())
    result = 0
    for i in range(n , -1, -2):
        result += pow(i,2)

    print(result)
    t -= 1

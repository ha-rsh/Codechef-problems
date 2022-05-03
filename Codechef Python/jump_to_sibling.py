from sys import stdin
from tkinter import N

t = int(stdin.readline().strip())
while t > 0:
    n = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().strip().split(' ')))
    new_arr = [None] * n
    new_arr[0] = 0
    temp = [None] * n
    temp[0] = 0
    maximum, result, count = 0, 0, 0
    if (arr[0] % 2) == (arr[n - 1] % 2):
        for i in range(1, n):
            if (arr[i] % 2) == (arr[0] % 2):
                result += 1
                
        print(result)

    else:
        for i in range(1, n):
            if (arr[0] % 2) != (arr[i] % 2): new_arr[i] = new_arr[i-1] + 1
            else: new_arr[i] = new_arr[i-1]

        result = new_arr[n-1]
        for i in range(1, n):
            if (arr[i] % 2) == (arr[0] % 2):
                count += 1
                result = min(result,count + new_arr[n-1] - new_arr[i])

        print(result)
    


    t -= 1

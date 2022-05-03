from re import A
from sys import stdin

t = int(stdin.readline().strip())
while t > 0:
    n, x = map(int, stdin.readline().strip().split())
    if n >= x: print("Yes")
    else:
        temp1 = (n//2) + 1
        temp2 = (n-temp1+1) * temp1
        if x > temp2:
            print("No")

        else:
            count = 0
            for i in range(1, n+1):
                if x%i == 0:
                    if n-i+1 >= (x/i):
                        count = 1
                        break
            
            if count:print("Yes")
            else: print("No")



    t -= 1


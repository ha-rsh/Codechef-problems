from sys import stdin
from collections import Counter

def building_tower():
    x, m = map(int,stdin.readline().strip().split(' '))
    temp = 2
    towers = 0
    while temp <= x:
        temp<<=1
        towers += 1

    temp /= 2
    temp2 = towers + 1
    if temp2 > m:
        print(0)
        return

    if temp == x:
       print(1 + (m-temp2))
    else:
       print(m-temp2)

t = int(stdin.readline().strip())
while t > 0:
    building_tower()    
    t -= 1


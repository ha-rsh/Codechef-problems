from sys import stdin

t = int(stdin.readline().strip())
while t > 0:
    n, k = map(int, stdin.readline().strip().split(' '))
    if n % 4 == 0:
        if k == 0: print("Off")
        else: print("On")
    
    else:
        state = n % 4
        if k == 0: print("On")
        else: print("Ambiguous")
        
    t -= 1
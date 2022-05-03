from sys import stdin

# declaring and taking input for the number of test cases
t = int(stdin.readline().strip())
while t > 0:
    n = int(stdin.readline().strip())
    count = 0
    for i in range(1, n + 1):     
        if i & 1:
            count += 1
    
    print(count)
    t -= 1
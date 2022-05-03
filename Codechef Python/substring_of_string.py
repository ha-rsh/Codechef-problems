from sys import stdin

# declaring and taking input for the number of test cases
t = int(stdin.readline().strip())

''' usingwhile loop to compute t test cases'''
while t > 0:
    ''' taking input for the string using 
        fast input method stdin'''
    s = stdin.readline().strip()
    op, val = 0, 0  # declaring count and val as 0

    ''' Iterating through the string'''
    for i in range(len(s)):          
        if s[i] != s[0] and s[i] != s[len(s) - 1]: op += 1
        else: op = 0
        val = max(val, op)      # assigning maximum value to val 

    print(-1) if val == 0 else print(val)
    t -= 1        

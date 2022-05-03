from sys import stdin

# declaring and taking input for the number of test cases
t = int(stdin.readline().strip())

''' Going through the t nimber of test
    cases using while loop'''
while t > 0:
    n = int(stdin.readline().strip())  # taking input for number of days
    if n < 6: print(0)  # if days are less than 6 then there will bw 0 holidays 
    else: print((n + 1) // 7)
    t -= 1
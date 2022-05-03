from sys import stdin

mod = 998244353

# declaring and taking input for the number of test cases
t = int(stdin.readline().strip())

''' usingwhile loop to compute t test cases'''
while t > 0:
    n = int(stdin.readline().strip())
    ''' taking input for the string using 
        fast input method stdin'''
    bin_string = stdin.readline().strip()

    ''' creating a list of size n and initially storing 
        0 at all the positions'''
    nums = [0] * n
    temp = 1  # creating and assigning temp variable as 1
    val = 0

    if bin_string[0] == '1': nums[0] = 1
    temp2 = nums[0]   # creating temp2 variable and initializing it the the 0th value store in numsay
    for i in range(1, n):
        if bin_string[i] == '1': temp2 += (i + 1)
        nums[i] = temp2 % 2

    for i in range(n-1, -1, -1):
        if nums[i] == 1:
            val += temp
            val %= mod
        temp *= 2
    temp %= mod
    print(val % mod)
    t -= 1
    
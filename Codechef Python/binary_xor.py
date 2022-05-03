from sys import stdin

def bin_xor(bin_str:str, n:int):
    arr = [None] * n
    one_count=0
    for i in range(n):
        arr[i]= bin_str[i]
        if arr[i]=='1':
            one_count += 1
    
    temp = 0
    zero_count = 0
    for i in range(n):
        if temp == arr[i]:
            zero_count += 1
            if temp == 1:
             temp = 0 
            
        else:temp = 1
    
    if one_count % 2 == 0:
        if one_count >= k and (one_count - k) % 2 == 0:
            print("Yes")
        else:
            if(zero_count >= k):
                print("Yes")
            else:print("No")

    else:
        if(one_count >= k and (one_count - k) % 2 == 0):
            print("Yes")
        else: print("No")

t = int(stdin.readline().strip())
while t > 0:
    n, k = map(int, stdin.readline().strip().split(" "))
    bin_str = stdin.readline().strip()
    bin_xor(bin_str=bin_str, n=n)
    t -= 1

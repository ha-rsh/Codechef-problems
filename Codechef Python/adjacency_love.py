from sys import stdin

t = int(stdin.readline().strip())
while t > 0:
    n = int(stdin.readline().strip())
    nums = list(map(int, stdin.readline().strip().split(' ')))
    odd_count = 0
    even_count = 0
    odd = []
    even = []
    for i in nums:
        if i & 1: 
            odd_count += 1
            odd.append(i)
        
        else:
            even_count += 1
            even.append(i)

    if odd_count == n and n & 1:print(-1)
    elif odd_count == 1 and even_count > 0: print(-1)
    elif odd_count == 1 and even_count == 0: print(odd[0])
    elif odd_count >=2 :
        if odd_count & 1: 
            print(odd[0], end=" ")
            for i in range(even_count):
                print(even[i], end=" ")

            for i in range(1, odd_count):
                print(odd[i], end=" ")
            
            print()
              
        else:
            for i in range(even_count):
                print(even[i], end=" ")
            
            for i in range(odd_count):
                print(odd[i], end=" ")

            print()     

    else:print(-1)
    t -= 1
from sys import stdin

t = int(stdin.readline().strip())
while t > 0:
    n = int(stdin.readline().strip())
    nums = list(map(int, stdin.readline().strip().split(' ')))
    odd = []
    even = []
    result = 0
    for i in range(n):
        if i & 1:
            odd.append(abs(nums[i]))
        
        else:
            even.append(abs(nums[i]))

    odd.sort()
    even.sort()
    if odd[len(odd) - 1] > even[0]:
        odd[len(odd) - 1], even[0] = even[0], odd[len(odd) - 1]

    for i in even:
        result += i
    
    for i in odd:
        result -= i

    print(result)

    t -= 1



from sys import stdin

t = int(stdin.readline().strip())
while t > 0:
    nums = list(map(int, stdin.readline().strip().split(' ')[:4]))
    nums.sort()
    xnum1 = (nums[2] + nums[0]) // 2
    ynum1= nums[2] - xnum1
    xnum2 = (nums[2] + nums[1]) // 2
    ynum2 = nums[2] - xnum2
    xnum3 = (nums[3] + nums[0]) // 2
    ynum3 = nums[3] - xnum3
    xnum4 = (nums[3] + nums[1]) // 2
    ynum4 = nums[3] - xnum4

    if (xnum1 % 1 == 0 ) and (xnum1 != 0) and (ynum1 % 1 == 0) and (ynum1 != 0):
        if ((xnum1 // ynum1) == nums[1]) and (xnum1 * ynum1 == nums[3]) and (xnum1 >= 1) and (ynum1 >= 1) and (xnum1 <= 10000) and (ynum1 <= 10000):
            print(xnum1, ynum1)
            continue
                
    if (xnum2 % 1 == 0) and (xnum2 != 0) and (ynum2 % 1 == 0) and (ynum2 != 0):
        if ((xnum2 // ynum2) == nums[0]) and (xnum2 * ynum2 == nums[3]) and (xnum2 >= 1) and (ynum2 >= 1) and (xnum2 <= 10000) and (ynum2 <= 10000):
            print(xnum2, ynum2)
            continue

    if (xnum3 % 1 == 0) and (xnum3 != 0) and (ynum3 % 1 == 0) and (ynum3 != 0):
        if ((xnum3 // ynum3) == nums[1]) and (xnum3 * ynum3 == nums[2]) and (xnum3 >= 1) and (ynum3 >= 1) and (xnum3 <= 10000) and (ynum3 <= 10000):
            print(xnum3, ynum3)
            continue
            
    if (xnum4 % 1 == 0) and (xnum4 != 0) and (ynum4 % 1 == 0) and (ynum4 != 0):
        if ((xnum4 // ynum4) == nums[0]) and (xnum4 * ynum4 == nums[2]) and (xnum4 >= 1) and (ynum4 >= 1) and (xnum4 <= 10000) and (ynum4 <= 10000):
            print(xnum4, ynum4)
            continue

    print(-1, -1)             
    t -= 1


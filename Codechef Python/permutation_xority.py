from sys import stdin

def perm_xor():
    n = int(stdin.readline().strip())
    nums = [None] * n
    if n == 2:
        print(-1)
        return

    if n %2 == 1:
        x = n
        for i in range(n):
            print(x, end=" ")
            x -= 1

        print()
        return

    x = 1
    for i in range(n):
        nums[i] = x
        x += 1

    nums[0] = 2
    nums[1] = 3
    nums[2] = 1
    for i in range(n):
        print(nums[i], end=" ")

    print()

t = int(stdin.readline().strip())
while t > 0:
    perm_xor()
    t -= 1

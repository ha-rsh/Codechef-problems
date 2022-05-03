from sys import stdin

def min_color(n:int, m:int, x1:int, y1:int, x2:int, y2:int):
    if (((x1 + y1) % 2) != ((x2 + y2) % 2)):
        for i in range(n):
            for j in range(m):
                ele = (i + j) % 2
                if ele == (x1 + y1) % 2: print(1, end=" ")
                else: print(2, end=" ")

            print()
        return

    mat_nums = [[None for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            ele = (i + j) % 2
            if ele == (x1 + y1) % 2: mat_nums[i][j] = 1
            else: mat_nums[i][j] = 2


    mat_nums[x1][y1] = 1
    mat_nums[x2][y2] = 2
    if x2 > 0: mat_nums[x2-1][y2] = 3 
    if x2 < n-1: mat_nums[x2+1][y2] = 3 
    if y2 > 0: mat_nums[x2][y2-1] = 3 
    if y2 < m-1: mat_nums[x2][y2+1] = 3 
    for i in range(n):
        for j in range(m):
            print(mat_nums[i][j], end=" ") 
        print()


t = int(stdin.readline().strip())
while t > 0:
    n, m = map(int, stdin.readline().strip().split(' '))
    x1, y1 = map(int, stdin.readline().strip().split(' '))
    x1 -= 1
    y1 -= 1
    x2, y2 = map(int, stdin.readline().strip().split(' '))
    x2 -= 1
    y2 -= 1
    min_color(n, m, x1, y1, x2, y2)
    t -= 1

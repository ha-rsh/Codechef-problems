from sys import stdin

t = int(stdin.readline().rstrip())
while t > 0:
    my_list = list(map(int, stdin.readline().strip().split(" ")))
    x = my_list[0]
    y = my_list[1]
    if x == 0 and y % 2 != 0:
        print('NO')
        
    elif (x + (y * 2)) % 2 == 0:
        print('YES')

    else:
        print('NO')
    t -= 1
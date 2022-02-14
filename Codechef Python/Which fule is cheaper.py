from sys import stdin

t = int(stdin.readline().rstrip())
while t > 0:
    my_list = list(map(int, stdin.readline().strip().split(" ")))
    x = my_list[0]
    y = my_list[1]
    a = my_list[2]
    b = my_list[3]
    k = my_list[4]
    for i in range(k):
        x = x + a
        y = y + b

    if x > y:
        print('DIESEL')
    elif x < y:
        print('PETROL')
    else:
        print('SAME PRICE')
    t -= 1
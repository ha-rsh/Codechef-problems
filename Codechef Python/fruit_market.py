from sys import stdin

t = int(stdin.readline().strip())
while t > 0:
    x, a, b, c = map(int, stdin.readline().strip().split())
    total_price = 0
    my_list = []
    my_list.append(a)
    my_list.append(b)
    my_list.append(c)
    my_list.sort()
    count = 0
    for i in range(x - 1):
        total_price += my_list[0]

    total_price += my_list[1]
    print(total_price)
    t -= 1


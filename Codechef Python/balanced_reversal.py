from sys import stdin

t = int(stdin.readline().strip())
while t > 0:
    n = int(stdin.readline().strip())
    str = stdin.readline().strip()
    number_of_one = 0
    number_of_zeros = 0
    for i in range(n):
        if str[i] == '0': number_of_zeros += 1
        else: number_of_one += 1

    new_str = ""
    for i in range(number_of_one):
        new_str += '1'

    for i in range(number_of_zeros):
        new_str += '0'

    new_str = new_str.sort(reverse=True)
    print(new_str)
    t -= 1



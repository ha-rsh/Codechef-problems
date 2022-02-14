from sys import stdin


t = int(stdin.readline().rstrip())
while t > 0:
    n = int(stdin.readline().rstrip())
    s = stdin.readline().rstrip()[:n]
    flag = True
    count1, count2 =0, 0
    for i in s:
        if i =='0':
            count1 += 1
        else:
            count2 += 1

    if (min(count1, count2)) == 0:
        flag = False

    if (min(count1, count2)) >= 2:
        move = count1 + count2 -(2*(min(count1,count2)))
        if move % 2 == 0:
            flag = False

    if flag:
        print('Alice')

    else:
        print('Bob')
    t -= 1
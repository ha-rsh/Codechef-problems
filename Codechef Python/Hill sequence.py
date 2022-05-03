from sys import stdin

t = int(stdin.readline().rstrip())
while t > 0:
    n = int(stdin.readline().rstrip())
    nums = list(map(int, stdin.readline().strip().split(' ')[:n]))
    my_dict = {}
    for i in range(n):
        if nums[i] in my_dict.keys():
             my_dict[nums[i]] += 1

        else:
            my_dict[nums[i]] = 1

    my_list = []
    f = 0
    for key, item in my_dict.items():
        if item > 2:
            f = 1
            break
        my_list.append(key)

    my_list.sort()
    if f == 1 or my_dict[my_list[len(my_list) - 1]] == 2:
        print(-1)

    else:
        for i in range(len(my_list)):
            if my_dict[my_list[i]] == 2:
                print(my_list[i], end=" ")

        for i in range(len(my_list)-1, -1, -1):
            print(my_list[i], end=" ")
        print()

    t -= 1
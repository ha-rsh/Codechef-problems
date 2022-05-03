from sys import stdin

def check_sort(string:list, n:int):
    i = 0
    j = len(string) - 1
    while i <= j:
        if string[i] > string[j]:
            string[i], string[j] = string[j], string[i]

        i += 1
        j -= 1

    flag = True

    i = 0
    j = 1
    while j < n:
        if string[i] > string[j]:
            flag = False
            break

        j += 1
        i += 1

    if flag:
        print("Yes")

    else:
        print("No")



t = int(stdin.readline().strip())
while t > 0:
    n = int(stdin.readline().strip())
    string = stdin.readline().strip()
    string = list(string)
    check_sort(string=string, n=n)
    t -= 1


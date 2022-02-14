from sys import stdin

t = int(stdin.readline().rstrip())
while t > 0:
    xk, yk = list(map(int, stdin.readline().strip().split(' ')))
    xr1, yr1 = list(map(int, stdin.readline().strip().split(' ')))
    xr2, yr2 = list(map(int, stdin.readline().strip().split(' ')))
    flag = None
    if xk != xr1  and xk != xr2 and yk != yr1 and yk != yr2:
        if (xk == 1 or xk == 8 or yk == 1 or yk == 8):
            if xk == 1:
                if (xr1 == 2 or xr2 == 2) and yr1 != yr2:
                    if abs(yk - yr1) > 1 and abs(yk- yr2) > 1:
                       flag = 1
            elif xk == 8:
                if (xr1 == 7 or xr2 == 7) and yr1 != yr2:
                    if abs(yk - yr1) > 1 and abs(yk - yr2) > 1:
                        flag = 1
            if yk == 1:
                if (yr1 == 2 or yr2 == 2) and xr1 != xr2:
                    if abs(xk-xr1) > 1 and abs(xk - xr2) > 1:
                        flag = 1
            elif yk == 8:
                if (yr1 == 7 or yr2 == 7) and xr1 != xr2:
                    if abs(xk-xr1) > 1 and abs(xk-xr2) > 1:
                        flag = 1
    else:
        flag = 0

    if flag: print("Yes")
    else: print("No")
    t -= 1


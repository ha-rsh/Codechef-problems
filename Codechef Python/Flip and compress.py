from sys import stdin

t = int(stdin.readline().rstrip())
while t > 0:
    s = stdin.readline().rstrip()
    v, ans, n = 0, 0, len(s)
    i = 0
    flag1 = flag2 = False
    while i < n:
        if s[i] == '0':
            if not flag1:
                flag1 = True
            else:
                if not flag2:
                    flag2 = True

        else:
            if flag1:
                if flag2:
                    if i < n-1:
                        if s[i + 1] == '0':
                            ans += 1
                        else:
                            ans += 2
                            flag1 = False
                            flag2 = False

                    else:
                        ans += 2
                        flag1 = False
                        flag2 = False

                else:
                    ans += 1
                    flag1 = False

        i += 1
    if flag1:
        if flag2:
            ans += 2
        else:
            ans += 1

    v = ans
    ans = 0
    i = 0
    flag1 = flag2 = False
    while i < n:
        if s[i] == '1':
            if not flag1:
                flag1 = True
            else:
                if not flag2:
                    flag2 = True

        else:
            if flag1:
                if flag2:
                    if i < n - 1:
                        if s[i + 1] == '1':
                            ans += 1
                        else:
                            ans += 2
                            flag1 = False
                            flag2 = False

                    else:
                        ans += 2
                        flag1 = False
                        flag2 = False

                else:
                    ans += 1
                    flag1 = False

        i += 1
    if flag1:
        if flag2:
            ans += 2
        else:
            ans += 1

    v = min(v, ans)
    print(v)
    t -= 1
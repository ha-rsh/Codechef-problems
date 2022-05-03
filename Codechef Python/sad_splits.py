from sys import stdin

def check_sub(n:list):
    even_count = 0
    odd_count = 0
    for i in range(len(n)):
       if n[i] % 2 == 0: even_count += 1
       else: odd_count += 1

    if n[len(n) - 1] & 1:
        if odd_count >= 2: print("Yes")
        else: print("No")

    else:
        if even_count >= 2: print("Yes")
        else: print("No")


t = int(stdin.readline().strip())
while t > 0:
    n= map(int,stdin.readline().strip())
    n = list(n)
    check_sub(n)
    t -= 1


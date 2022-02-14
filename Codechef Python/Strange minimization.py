import math

compute_lcm = lambda x, y: x * y // math.gcd(x, y)
t = int(input())
for t_itr in range(t):
    n = int(input())
    p = 1
    current_min = 10**20
    out = (n, n+1)
    while p * p <= n:
        if n % p == 0: 
            flag1 = abs(compute_lcm(n, n+p) - math.gcd(n, n+p))
            flag2 = flag1 + 1
            if (n + n//p != 2*n):
                flag2 = abs(compute_lcm(n, n+ (n//p)) - math.gcd(n, n + (n//p)))
            cpl = (n, n + p)
            if flag2 <= flag1:
                cpl = (n, n + (n//p))
            flag = min(flag1, flag2)
            if flag <= current_min:
                out = cpl
                current_min = min(current_min, flag)
        p +=1
    print(out[1])
from sys import stdin

n, atm=list(map(float,input().split()))
n = int(n)
if (n + 0.50<=atm and n % 5==0):
    result = float(atm-n-0.5)
else:
    result = float(atm)

print("{0:.2f}".format(result))

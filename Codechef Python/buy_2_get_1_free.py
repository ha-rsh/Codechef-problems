from sys import stdin

def buy_items(n:int, x:int):
    var1 = (n % 3) * x
    var2 = (n // 3) * x
    print(var1 + (var2 * 2))

t = int(stdin.readline().strip())
while t > 0:
    n, x = map(int, stdin.readline().strip().split(' '))
    buy_items(n, x)
    t -= 1
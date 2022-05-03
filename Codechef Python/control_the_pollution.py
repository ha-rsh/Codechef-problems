from sys import maxsize, stdin
import math

t = int(stdin.readline().strip())
while t > 0:
    n, x, y = map(int, stdin.readline().strip().split(" "))
    minimum = maxsize
    for bus in range(0, 11):
        car = (n - (100 * bus)) / 4
        if car < 0: car = 0
        else: car = math.ceil(car)

        value = (car * y) + (bus * x)
        minimum = min(minimum, value)

    print(minimum)
    t -= 1


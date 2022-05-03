from sys import stdin 

t = int(stdin.readline().strip())
while t > 0:
    n = int(stdin.readline().strip())
    nums = list(map(int, stdin.readline().strip().split(' ')))
    holiday_days = [6, 13, 20, 27, 7 ,14, 21, 28]
    holidays = len(holiday_days)
    for i in nums:
        if i not in holiday_days:
            holidays += 1

    print(holidays)
    t -= 1
    
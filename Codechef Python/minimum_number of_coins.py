from sys import stdin

def min_coins(x: int):
    if x % 5 != 0:
        print(-1)
        return

    ele = x // 5
    number_of_five_coins = 0
    number_of_ten_coins = 0

    if ele & 1:
        ans = ele - 1
        number_of_ten_coins += ans // 2
        number_of_five_coins += 1

    elif ele & 1 == 0:
        number_of_ten_coins += ele // 2
        number_of_five_coins += 0

    final_ans = number_of_five_coins + number_of_ten_coins
    print(final_ans)

t = int(stdin.readline().strip())
while t > 0:
    x = int(stdin.readline().strip())
    min_coins(x)
    t -= 1


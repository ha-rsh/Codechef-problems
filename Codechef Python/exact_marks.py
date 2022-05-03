from sys import stdin

def ans_check(correct_ans:int, incorrect_ans:int, unattempted_ans:int, x:int, n:int):
    if x % 3 == 0: correct_ans += x // 3
    elif x % 3 == 1:
        correct_ans += (x // 3) + 1
        incorrect_ans += 2

    elif x % 3 == 2:
        correct_ans += (x // 3) + 1
        incorrect_ans += 1

    if correct_ans + incorrect_ans <= n:
        print("YES")
        print(correct_ans, incorrect_ans, n - correct_ans - incorrect_ans)

    else: print("NO")

# declaring and taking input for the number of test cases
t = int(stdin.readline().strip())
while t > 0:
    n, x = map(int,stdin.readline().strip().split(' '))
    correct_ans, incorrect_ans, unattempted_ans = 0, 0, 0
    ans_check(correct_ans=correct_ans, incorrect_ans=incorrect_ans, unattempted_ans=unattempted_ans , x=x, n=n)
    t -= 1
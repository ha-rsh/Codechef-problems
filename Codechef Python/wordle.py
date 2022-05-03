from sys import stdin

t = int(stdin.readline().strip())
while t > 0:
    hidden = stdin.readline().strip()
    guess = stdin.readline().strip()
    ans = ""
    for i in range(len(hidden)):
        if hidden[i] == guess[i]: ans += "G" 
        else: ans += "B"

    print(ans)
    t -= 1

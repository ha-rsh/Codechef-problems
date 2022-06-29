from operator import itemgetter
from sys import maxsize, stdin
from collections import Counter, defaultdict

t = int(stdin.readline().strip())
while t > 0:
    n = int(stdin.readline().strip())
    ans = ""
    if n % 2 == 0:
        ans += "10"
        for i in range(n - 4):
          ans += "0"

        ans += "01"


    else: 
        for i in range(0, n):
          if i % 2 == 0:ans += "0"
          else: ans += "1"
    
    print(ans)
    t -= 1
    
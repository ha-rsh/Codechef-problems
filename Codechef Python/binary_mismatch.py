from sys import stdin

def bin_mismatch(bin_str:str, n:int):
    one_check = dict()
    zero_check = dict()
    val = 0
    flag = 0
    if n % 2: print("No")
    else:
        for i in range(n):
            if(bin_str[i] == '1'):
                    one_check[i+1] = 1 + one_check[i]
                    zero_check[i+1] = zero_check[i]
            else:
                one_check[i+1] = one_check[i]
                zero_check[i+1] = zero_check [i] + 1

        if(zero_check[n] > one_check [n]):
                val = (zero_check[n] - one_check[n]) // 2 
                for i in range(1, n + 1):
                    if(zero_check[i] - one_check[i] == val):
                        print("Yes")
                        flag = 1
                        print("1 ", i)
                        break
                if(flag==0):
                    print("No")

        elif zero_check[n] < one_check[n]:
                val = (one_check[n] - zero_check[n]) // 2
                for i in range(1, n +1):
                    if(one_check[i] - zero_check[i] == val):
                        print("Yes")
                        flag = 1
                        print("1 ", i)
                        break
                if(flag==0):
                    print("No")
    
        else:
                print("Yes")
                print("1 ", n)

# declaring and taking input for the number of test cases
t = int(stdin.readline().strip())
while t > 0:
    n = int(stdin.readline().strip())
    bin_string = stdin.readline().strip()
    bin_mismatch(bin_str=bin_string, n=n)
    t -= 1


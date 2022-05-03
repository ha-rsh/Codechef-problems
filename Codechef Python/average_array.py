from sys import stdin

# declaring and taking input for the number of test cases
t = int(stdin.readline().strip())
while t > 0:
    n, mean_value = map(int, stdin.readline().strip().split(' '))
    if n % 2:
        print(mean_value, end=" ")
        for i in range(1, (n//2) + 1):
            print(mean_value + i, mean_value - i, end=" ")

        print()

    else:
        for i in range(1, (n//2) + 1):
            print(mean_value + i, mean_value - i, end=" ") 
        print() 

    t -= 1

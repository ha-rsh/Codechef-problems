from sys import stdin

a,b,x,y = map(int, stdin.readline().strip().split(' '))
total_cost = ((a*x)+(b*y))
print(total_cost)
from sys import stdin

def swap_parity(bin_str: list):


t = int(stdin.readline().strip())
while t > 0:
    n = int(stdin.readline().strip())
    string = stdin.readline().strip()
    string = list(string)
    swap_parity(bin_str=string)
    t -= 1

from sys import stdin

def flip_sorting(bin_str:list):
    if bin_str == sorted(bin_str):
        print(0)
        return

    output = [] 

    for i in range(len(bin_str) - 1, -1, -1):
      if bin_str[i] == '0':
        temp = i + 1
        for k in range(i +1):
          if bin_str[k] == '1': bin_str[k] = '0'
          else: bin_str[k] = '1'

        output.append((1,temp))
    
    print(len(output))
    for i in range(len(output)):
      print(output[i][0], output[i][1])


t = int(stdin.readline().strip())
while t > 0:
    n = int(stdin.readline().strip())
    string = stdin.readline().strip()
    string = list(string)
    flip_sorting(bin_str=string)
    t -= 1

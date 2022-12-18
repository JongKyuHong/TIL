import sys
import math
input = sys.stdin.readline

while 1:
    n = int(input())
    if n == -1:
        break
    res = []
    for i in range(1, n):
        if n % i == 0:
            res.append(i)
    #print(res)
    if sum(res) == n:
        print(f'{n} = ', end='')
        for i in range(len(res)):
            if i == len(res)-1:
                print(f'{res[i]}')
            else:
                print(f'{res[i]} + ',end='')
    else:
        print(f'{n} is NOT perfect.')

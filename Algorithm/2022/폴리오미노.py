import sys

input = sys.stdin.readline
board = list(input())

poly = 0
res = ''
for i in board:
    if i == '.':
        if poly == 2:
            res += 'BB'
        elif poly % 2:
            print(-1)
            exit()
        res += '.'
        poly = 0
    elif i == 'X':
        poly += 1
        if poly == 4:
            poly = 0
            res += 'AAAA'

if poly == 3 or poly == 1:
    print(-1)
elif poly == 2:
    res += 'BB'
    print(res)
else:
    print(res)
        
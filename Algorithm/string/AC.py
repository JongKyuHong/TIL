import sys
from collections import deque

input = sys.stdin.readline


for _ in range(int(input())):
    p = input().strip()
    n = int(input())
    array = deque(input().rstrip()[1:-1].split(','))
    if n == 0:
        array = []
    r_flag = True
    flag = 0
    for i in p:
        if i == 'R':
            r_flag = not r_flag  # r_flag1TRUE일때 정방향, FALSE일때 역방향으로 생각
        else:
            if array:
                if r_flag:
                    array.popleft()
                else:
                    array.pop()
            else:
                flag = 1

    if p.count('R') % 2:
        array.reverse()
    if flag == 0:
        print('['+','.join(array)+']')
    else:
        print('error')

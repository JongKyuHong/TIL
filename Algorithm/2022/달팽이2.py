from collections import deque
import sys 
input = sys.stdin.readline

m, n = map(int, input().split())
cnt = 0
dir = 0
while m != 1 and n != 1:
    if dir == 0:
        m -= 1
        cnt += 1
    elif dir == 1:
        n -= 1
        cnt += 1
    elif dir == 2:
        m -= 1
        cnt += 1
    else:
        n -= 1
        cnt += 1
    dir += 1
    dir %= 4
print(cnt+1)
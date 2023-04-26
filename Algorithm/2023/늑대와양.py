from collections import deque
import sys
input = sys.stdin.readline
delta = ((0,1),(0,-1),(1,0),(-1,0))

def find():
    for i, j in sheep:
        for dr, dc in delta:
            nr, nc = dr+i, dc+j
            if 0 <= nr < R and 0 <= nc < C and lst[nr][nc] != 'S':
                if lst[nr][nc] == 'W':
                    return False
                else:
                    lst[nr][nc] = 'D'
    return True

R, C = map(int, input().split())
lst = []
for _ in range(R):
    lst.append(list(input().rstrip()))

sheep = []
wolf = []
for i in range(R):
    for j in range(C):
        if lst[i][j] == 'S':
            sheep.append([i, j])
        elif lst[i][j] == 'W':
            wolf.append([i, j])
if find():
    print(1)
    for i in lst:
        for j in i:
            print(j, end='')
        print()
else:
    print(0)


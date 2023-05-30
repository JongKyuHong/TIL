from collections import deque
import sys
input = sys.stdin.readline
delta = ((0, 1), (1, 0), (0, -1), (-1, 0))

def find(q):
    tmp = deque()
    while q:
        r, c = q.popleft()
        if r == end[0] and c == end[1]:
            return 1, None
        for dr, dc in delta:
            nr, nc = dr+r, dc+c
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                if lst[nr][nc] == 'X':
                    tmp.append((nr, nc))
                else:
                    q.append((nr, nc))
                visited[nr][nc] = 1
    return 0, tmp

def melt_ice(water):
    next_water = deque()
    while water:
        r, c = water.popleft()
        for dr, dc in delta:
            nr, nc = dr+r, dc+c
            if 0 <= nr < R and 0 <= nc < C and lst[nr][nc] == 'X':
                next_water.append((nr, nc))
                lst[nr][nc] = '.'
    return next_water

R, C = map(int, input().split())
start, end = [], []
lst = []
water = deque()
for i in range(R):
    input_ = list(input().rstrip())
    for j in range(C):
        if input_[j] == '.' or input_[j] == 'L':
            water.append((i, j))
        if input_[j] == 'L':
            if not start:
                start = [i, j]
            else:
                end = [i, j]
            input_[j] = '.'
    lst.append(input_)

time = 0
visited = [[0]*C for _ in range(R)]
q = deque()
q.append((start[0], start[1]))
visited[start[0]][start[1]] = 1
while 1:
    res, q = find(q)
    if res:
        break
    water = melt_ice(water)
    time += 1

print(time)
import sys
input = sys.stdin.readline

h, w, x, y = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(h+x)]
start_r, start_c = 0, 0
flag = 0
for i in range(h+x):
    for j in range(w+y):
        if lst[i][j]:
            start_r, start_c = i, j
            flag = 1
            break
    if flag:
        break
graph = [[0]*w for _ in range(h)]

for i in range(start_r, start_r+h):
    for j in range(start_c, start_c+w):
        graph[i][j] = lst[i][j]

for i in range(start_r+x, start_r+h):
    for j in range(start_c+y, start_c+w):
        graph[i][j] -= graph[i-x][j-y]

for i in graph:
    print(*i)
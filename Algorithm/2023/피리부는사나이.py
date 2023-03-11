from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maps = [list(input().rstrip()) for _ in range(N)]
parent = [i for i in range(N*M)]

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

for num in range(N*M):
    x = num%M
    y = num//M
    if maps[y][x] == 'D':
        nr, nc = y+1, x
    elif maps[y][x] == 'U':
        nr, nc = y-1, x
    elif maps[y][x] == 'L':
        nr, nc = y, x-1
    else:
        nr, nc = y, x+1
    next_num = nr*M + nc
    if next_num < 0 or next_num >= N*M:
        continue
    union(num, next_num)
ans = 0
visited = dict()
for i in range(N*M):
    if find(parent[i]) not in visited:
        ans += 1
        visited[parent[i]] = 1
print(ans)

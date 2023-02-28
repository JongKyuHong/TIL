from collections import deque
import sys
input = sys.stdin.readline
delta = ((0,1),(0,-1),(1,0),(-1,0))

def bfs(i, j):
    q = deque()
    q.append((i,j))
    #tmp = [[i,j]]
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr, nc = dr+r, dc+c
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and maps[nr][nc] == 1:
                visited[nr][nc] = visited[i][j]
                q.append((nr, nc)) 
                #tmp.append([nr,nc])
    #return tmp

def find_island(r, c):
    for dr, dc in delta:
        r1, c1 = r, c
        nr, nc = dr+r1, dc+c1
        cnt = 0
        while 0 <= nr < N and 0 <= nc < M:
            if visited[nr][nc] != 0 and visited[nr][nc] != visited[r][c]:
                island.append((cnt, visited[r][c], visited[nr][nc]))
                break
            elif visited[nr][nc] == 0:
                cnt += 1
            elif visited[nr][nc] == visited[r][c]:
                break
            r1, c1 = nr, nc
            nr,nc = dr+r1, dc+c1

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
cnt = 1
for i in range(N):
    for j in range(M):
        if maps[i][j] == 1 and not visited[i][j]:
            visited[i][j] = cnt
            cnt += 1
            bfs(i, j)

# island의 겉 8군데를 저장해놓고 일직선으로 쏠때 몇명이 걸리는지?

island = []
for i in range(N):
    for j in range(M):
        if maps[i][j] == 1:
            find_island(i, j)
parent = [i for i in range(cnt)]
island.sort()
result = 0
flag = 1
for cost, a, b in island:
    if cost >= 2:
        if find(a) != find(b):
            union(a, b)
            result += cost
            flag += 1
print(result if flag == cnt-1 else -1)
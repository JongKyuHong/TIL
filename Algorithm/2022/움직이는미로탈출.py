from collections import deque
import sys
input = sys.stdin.readline

delta = ((0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1))

def bfs(r, c):
    q = deque()
    visited[r][c] = 1
    q.append((r, c))
    while q:
        r, c = q.popleft()
        if r == 0 and c == 7:
            return 1
        for dr, dc in delta:
            nr, nc = dr+r, dc+c
            if 0 <= nr < 8 and 0 <= nc < 8 and not graph[nr][nc]:
                if not visited[nr-1][nc] and not graph[nr-1][nc]:
                    visited[nr-1][nc] = 1
                    q.append((nr-1,nc))
    return 0
graph = []
for _ in range(8):
    data = input()
    data2 = []
    for i in data:
        if i =='.':
            data2.append(0)
        else:
            data2.append(1)
    graph.append(data2)

visited = [[0 for _ in range(8)] for _ in range(8)]
a = bfs(7,0)
if a:
    print(1)
else:
    print(0)


from collections import deque
import sys
input = sys.stdin.readline

delta = ((0,1),(0,-1),(1,0),(-1,0))
def bfs(r, c, val):
    q = deque()
    q.append((r, c))
    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr, nc = dr+r, dc+c
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and graph[nr][nc]:
                visited[nr][nc] = val
                q.append((nr, nc))

n, m = map(int, input().split()) # 세로, 가로
graph = []
for i in range(n):
    data2 = list(map(int, input().split()))
    ans = []
    for j in range(0, len(data2), 3):
        ans.append((data2[j] + data2[j+1] + data2[j+2])/3)
    graph.append(ans)


T = int(input())

cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] >= T:
            graph[i][j] = 255
        else:
            graph[i][j] = 0


visited = [[0]*m for _ in range(n)]
num = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] and not visited[i][j]:
            num += 1
            visited[i][j] = num
            bfs(i, j, num)
        
print(num)
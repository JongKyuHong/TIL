from collections import deque
import sys 
input = sys.stdin.readline

n, m, v = map(int, input().split())
edges = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
    edges[a].sort()
    edges[b].sort()
path = []
def dfs(start):
    path.append(start)
    for i in edges[start]:
        if not visited[i]:
            visited[i] = 1
            dfs(i)

visited = [0]*(n+1)
visited[v] = 1
dfs(v)
print(*path)
path = []
def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        now = q.popleft()
        path.append(now)
        for i in edges[now]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)
visited = [0]*(n+1)
bfs(v)
print(*path)
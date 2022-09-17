from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    q = deque()
    q.append(start)
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)

n, m = map(int, input().split()) # 정점의 갯수, 도로의 갯수

graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n+1)
bfs(1)

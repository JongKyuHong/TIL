from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split()) # 정점의갯수, 간선의갯수, 탐색을 시작할 정점의 번호
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

def dfs(node):
    print(node, end=' ')
    for i in graph[node]:
        if not visited[i]:
            visited[i] = 1
            dfs(i)

visited[v] = 1
dfs(v)
visited = [0]*(n+1)
visited[v] = 1
print()
q = deque()
q.append(v)
while q:
    node = q.popleft()
    print(node, end=' ')
    for i in graph[node]:
        if not visited[i]:
            visited[i] = 1
            q.append(i)
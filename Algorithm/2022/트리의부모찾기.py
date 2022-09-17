from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n+1)

def bfs():
    q = deque([])
    q.append(1)
    while q:
        now = q.popleft()
        for next_node in graph[now]:
            if visited[next_node] == 0:
                visited[next_node] = now
                q.append(next_node)

bfs()
for i in range(2,n+1):
    print(visited[i])
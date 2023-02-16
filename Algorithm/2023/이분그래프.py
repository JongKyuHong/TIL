from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, group):
    q = deque([start])
    visited[start] = group
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = -1*visited[now]
                q.append(i)
            elif visited[i] == visited[now]:
                return 0
    return 1

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0]*(V+1)
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, V+1):
        if not visited[i]:
            result = bfs(i, 1)
            if not result:
                break

    print('YES' if result else 'NO')
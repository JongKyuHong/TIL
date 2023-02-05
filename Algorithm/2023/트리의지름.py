from collections import deque
import sys
input = sys.stdin.readline

V = int(input())
graph = [[]*(V+1) for _ in range(V+1)]
for _ in range(V):
    inp = list(map(int, input().split()))
    node = inp[0]
    for i in range(1, len(inp)-2, 2):
        graph[node].append([inp[i+1], inp[i]])

def bfs(start):
    visited = [-1]*(V+1)
    q = deque()
    q.append(start)
    visited[start] = 0
    _max = [0, 0]
    while q:
        now = q.popleft()
        for cost, next in graph[now]:
            if visited[next] == -1:
                visited[next] = visited[now] + cost
                q.append(next)
                if _max[0] < visited[next]:
                    _max = visited[next], next
    return _max
dis, node = bfs(1)
dis, node = bfs(node)
print(dis)
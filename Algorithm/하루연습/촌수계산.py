from collections import deque

def bfs(node):
    q = deque()
    q.append(node)
    while q:
        node = q.popleft()
        for i in graph[node]:
            if check[i] == 0:
                check[i] = check[node] + 1
                q.append(i)

n = int(input())
graph = [[] for _ in range(n+1)]
s, e = map(int, input().split())
for _ in range(int(input())):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
check = [0]*(n+1)
bfs(s)
print(check[e] if check[e] > 0 else -1)
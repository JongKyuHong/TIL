from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, adj):
    rtn = 0
    q = deque()
    q.append(x)
    visited[x] = 1
    while q:
        v = q.popleft()
        for n in adj[v]:
            if not visited[n]:
                q.append(n)
                visited[n] = 1
                rtn += 1
    return rtn

N, M, X = map(int, input().split())
higher = [[] for _ in range(N+1)] 
lower = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(M):
    a, b = map(int, input().split())
    higher[a].append(b)
    lower[b].append(a)

print(1+bfs(X, lower), N-bfs(X, higher))
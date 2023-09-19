from collections import deque
import sys 
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])        
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a > b:
        parent[a] = b 
    else:
        parent[b] = a

def bfs(idx):
    q = deque()
    q.append(idx) # 아직 부모의 그게 안들어있는 친구
    idx = parent[idx]
    while q:
        now = q.popleft()
        for i in lst[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1
                parent[i] = idx

N, M = map(int, input().split())
parent = [i for i in range(N+1)]
lst = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    lst[u].append(v)
    lst[v].append(u)
    if parent[u] != parent[v]:
        union(u, v)

visited = [0]*(N+1)
result = []
for i in range(1, N+1):
    if not visited[i] and parent[i] not in result:
       bfs(i)
       result.append(parent[i])
print(len(result))
    

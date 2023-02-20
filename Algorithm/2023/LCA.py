import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())

parent = [0]*(N+1)
d = [0]*(N+1)
c = [0]*(N+1)
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x, depth):
    c[x] = 1
    d[x] = depth
    for y in graph[x]:
        if c[y]:
            continue
        parent[y] = x
        dfs(y, depth+1)

def lca(a, b):
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]
    while a != b:
        a = parent[a]
        b = parent[b]
    return a

dfs(1, 0)

M = int(input())
for i in range(M):
    a, b = map(int, input().split())
    print(lca(a, b))
    
            
